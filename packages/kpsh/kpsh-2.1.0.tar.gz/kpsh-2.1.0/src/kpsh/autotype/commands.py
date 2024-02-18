# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2019 Michał Góral.

import time
import re
import subprocess


def _token_delay(token):
    match = re.match(r"{DELAY (\d+)}", token)
    if match:
        delay = match.group(1)
        return lambda t=delay: time.sleep(int(t) / 1000)
    return None


_COMMANDS = [
    _token_delay,
]


def run_command(token):
    for checker in _COMMANDS:
        cmd = checker(token)
        if callable(cmd):
            cmd()
            return True
    return False


def _tool(cmd, *args):
    cmd = [cmd]
    cmd.extend(args)
    subprocess.run(cmd)


def xdotool_type(delay, arg):
    _tool("xdotool", "type", "--delay", delay, "--", arg)


def xdotool_key(delay, key):
    _tool("xdotool", "key", "--clearmodifiers", "--delay", delay, "--", key)


def ydotool_type(delay, arg):
    _tool("ydotool", "type", "--key-delay", delay, "--", arg)


def ydotool_key(delay, key):
    _tool("ydotool", "key", "--key-delay", delay, "--", key)


def wtype_type(delay, arg):
    def _cmd(ch):
        if ch == "-":
            return ["-k", "minus"]
        return [ch]

    args = []
    for ch in arg:
        args.extend(_cmd(ch))
        args.extend(["-s", delay])

    _tool("wtype", *args)


def wtype_key(delay, key):
    _tool("wtype", "-k", key, "-s", delay)
