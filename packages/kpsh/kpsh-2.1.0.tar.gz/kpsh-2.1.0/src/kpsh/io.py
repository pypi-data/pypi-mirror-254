import os
import sys
import shlex
from functools import lru_cache
from contextlib import contextmanager
import socket
import stat
import struct
import select
import pwd
import grp

from prompt_toolkit import PromptSession
from prompt_toolkit import prompt as input_prompt
from prompt_toolkit.formatted_text.html import HTML

from kpsh.commands import CommandError, ArgumentParserError
from kpsh.completion import CommandCompleter


class Handler:
    def __init__(self):
        self._run = True
        self._returncode = 0

    def prompt(self, prompt="", is_password=False):
        """Used to prompt for any kind of input"""
        return None

    def print(self, *a, **kw):
        """Used to print ordinary messages"""
        print(*a, **kw)

    def eprint(self, *a, **kw):
        """Used to print error messages"""
        kw["file"] = sys.stderr
        print(*a, **kw)

    def get_command(self, kp):
        """Called when handler is ready to accept a next command. Returns a
        unparsed argument-like string. Children should override this method to
        read user input."""
        return None

    def finalize_command(self):
        """Always called after each command ends."""
        pass

    def initialize(self, kp):
        """Called before Handler enters its command loop."""
        pass

    def teardown(self, kp):
        """Called after Handler exits its command loop."""
        pass

    def stop(self, returncode=0):
        """Used to stop the running command loop."""
        self._run = False
        self._returncode = returncode

    def run(self, kp, cmd_parser):
        with self._setup(kp):
            while self._run:
                text = self.get_command(kp)
                if not text:
                    continue

                try:
                    cmd = shlex.split(text)
                except ValueError as e:
                    self.eprint("Command syntax error: {}.".format(str(e)))
                    continue

                if not cmd:
                    continue

                try:
                    cargs = cmd_parser.parse_args(cmd)
                    cargs.func(kp, cargs, self)
                except ArgumentParserError as e:
                    self.eprint(str(e))
                except CommandError as e:
                    self.eprint(str(e))
                finally:
                    self.finalize_command()
        return self._returncode

    @contextmanager
    def _setup(self, kp):
        self.initialize(kp)
        try:
            yield
        except KeyboardInterrupt:
            self.stop(1)
        finally:
            self.teardown(kp)


class Interactive(Handler):
    def __init__(self, prompt, parsers):
        self._session = None
        self._prompt = prompt
        self._parsers = parsers
        super().__init__()

    def initialize(self, kp):
        compl = CommandCompleter(kp, (p for p in self._parsers if p))
        self._session = PromptSession(completer=compl, complete_while_typing=False)

    def get_command(self, kp):
        try:
            return self._session.prompt(self._ps1(kp.db))
        except KeyboardInterrupt:
            return None
        except EOFError:
            self.stop()
            return None

    def prompt(self, prompt="", is_password=False):
        try:
            return input_prompt(prompt, is_password=is_password)
        except (EOFError, KeyboardInterrupt):
            return None

    @lru_cache(maxsize=32)
    def _ps1(self, dbpath):
        if not dbpath:
            dbpath = ""
        home = os.path.expanduser("~")
        if dbpath.startswith(home):
            dbpath = dbpath.replace(home, "~")

        return HTML(self._prompt.format(dbpath))


class NonInteractive(Handler):
    def __init__(self):
        self._read_input = False
        super().__init__()

    def get_command(self, kp):
        try:
            return input()
        except EOFError:
            self.stop()
            return None


class Arguments(Handler):
    def __init__(self, commands):
        self._iter = iter(commands)
        super().__init__()

    def get_command(self, kp):
        try:
            return next(self._iter)
        except StopIteration:
            self.stop()
            return None


class Daemon(Handler):
    def __init__(self, path):
        self._path = path
        super().__init__()

    def initialize(self, kp):
        self._serv = _SocketServer(self._path)

    def teardown(self, kp):
        self._serv.stop()

    def prompt(self, prompt="", is_password=False):
        if is_password:
            resptype = "PS"
        else:
            resptype = "P"

        msg = "{} {}".format(resptype, prompt)
        self._send(msg)
        return self._recv()

    def print(self, *a, **kw):
        msg = "M {}".format(" ".join(str(arg) for arg in a))
        self._send(msg)

    def eprint(self, *a, **kw):
        msg = "E {}".format(" ".join(a))
        self._send(msg)

    def get_command(self, kp):
        return self._recv()

    def finalize_command(self):
        self._send("OK")

    def _recv(self):
        return _recv(self._serv)

    def _send(self, msg):
        _send(msg, self._serv)


class _SocketServer:
    """Wrapper for all hairy socket stuff"""

    def __init__(self, path):
        self._socket_path = path

        self._close_remote_kpsh()
        self._remove_socket()

        sock_denials = (
            stat.S_IRGRP
            | stat.S_IWGRP
            | stat.S_IXGRP
            | stat.S_IROTH
            | stat.S_IWOTH
            | stat.S_IXOTH
        )

        self._sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        with _umask(sock_denials):
            self._sock.bind(self._socket_path)
        self._sock.listen(1)
        self._conn = None

    def send(self, msg):
        if not self._conn:
            return

        msglen = len(msg)
        totalsent = 0
        while totalsent < msglen:
            try:
                sent = self._conn.send(msg[totalsent:msglen])
            except BrokenPipeError:
                sent = 0

            if sent == 0:
                self._close_conn()
                return
            totalsent += sent

    def recv(self, size):
        self._wait_for_client()
        buf = self._conn.recv(size)
        if not buf:
            self._close_conn()
            return None
        return buf

    def stop(self):
        self._close_conn()

        if self._sock:
            self._sock.shutdown(socket.SHUT_RDWR)
            self._sock.close()
            self._sock = None

        self._remove_socket()

    def _accept(self):
        conn, _ = self._sock.accept()
        return conn

    def _wait_for_client(self):
        while not self._conn:
            self._conn = self._accept()
            creds = self._conn.getsockopt(
                socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize("3i")
            )
            pid, uid, gid = struct.unpack("3i", creds)

            if not _verify_credentials(uid):
                _send("E Permission denied", self)
                self._close_conn()

        while True:
            # Server continuously accepts all connections because queuing them
            # on listen() is unreliable - it's impossible to tell how listen(0)
            # behaves. Certainly it queues at least 1 non-accepted connection,
            # which might block clients forever. So we'll just wait on
            # select() whenever blocking socket operation occurs and close all
            # connections but the first one. Clients should notice broken
            # connection with first recv().
            readable, _, _ = select.select([self._conn, self._sock], [], [])
            if self._sock in readable:
                self._accept().close()
            if self._conn in readable:
                break

    def _close_conn(self):
        if not self._conn:
            return

        self._conn.close()
        self._conn = None

    def _close_remote_kpsh(self):
        # This method tries to gracefully close remote kpsh instance which uses
        # the requested socket
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.settimeout(5.0)

            try:
                sock.connect(self._socket_path)
            except (FileNotFoundError, ConnectionRefusedError) as e:
                return

            msg = "exit"
            data = msg.encode()
            msglen = struct.pack("!i", len(data))
            sock.send(msglen)
            sock.send(data)

            # block until the remote end exits; without this, we could have
            # ended with a socket removed when remote cleans itself
            sock.recv(1)

    def _remove_socket(self):
        try:
            os.remove(self._socket_path)
        except FileNotFoundError:
            pass


def _verify_credentials(uid):
    """Compare credentials against kpsh's ones. KPSH uses its own effective
    UID/GID. When _verify_credentials is called with credentials obtained via
    SO_PEERCRED, they will be effective UID/GID of the client process as well
    ("those  that  were in effect at the time of the call to connect(2)" - from
    `man unix`)"""

    myuid = os.geteuid()
    mygid = os.getegid()

    try:
        mygid_members = grp.getgrgid(mygid).gr_mem
    except KeyError:
        mygid_members = []

    try:
        uid_name = pwd.getpwuid(uid).pw_name
    except KeyError:
        uid_name = None

    return myuid == uid or uid_name in mygid_members


def _send(msg, serv):
    """Send a message which is correct according to the kpsh daemon protocol:
    | msglen (integer, 4 bytes) | msg (encoded string, msglen butes) |
    """
    data = msg.encode()
    msglen = struct.pack("!i", len(data))
    serv.send(msglen)
    serv.send(data)


def _recv(serv):
    """Receive a message, expecting that it is correct according to kpsh
    protocol. See _send() for the details of the protocol."""
    buf = serv.recv(4)
    if not buf:
        return None

    msglen = struct.unpack("!i", buf)[0]
    if msglen == 0:
        return None

    data = serv.recv(msglen)
    if not data:
        return None

    return data.decode()


@contextmanager
def _umask(mask: int):
    oldmask = os.umask(mask)
    try:
        yield
    finally:
        os.umask(oldmask)
