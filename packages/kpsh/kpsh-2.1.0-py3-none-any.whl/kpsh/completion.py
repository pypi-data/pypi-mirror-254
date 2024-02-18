import os
import glob
import re
import shlex
from collections import namedtuple

from prompt_toolkit.completion import Completer, Completion

Word = namedtuple("Word", ("index", "text", "has_errors"))
_QUOTES = "'\""


class CompleteWord:
    def __init__(self, word, meta=None):
        self.word = word
        self.meta = meta

    def __eq__(self, other):
        return self.word == other.word

    def __lt__(self, other):
        return self.word < other.word


class CommandCompleter(Completer):
    def __init__(self, kp, commands):
        self._commands = sorted(commands)
        self._kp = kp

    def get_completions(self, document, complete_event):
        text_before = document.text_before_cursor
        if " " in text_before:
            command = text_before.partition(" ")[0]
            fn = getattr(self, "_{}".format(command), None)
            if callable(fn):
                yield from fn(document)
        else:
            yield from self._complete_commands(document)

    def _complete_commands(self, document):
        text_before = document.text_before_cursor
        for command in self._commands:
            if command.startswith(text_before):
                yield Completion(command, -len(text_before))

    def _show(self, document):
        opts = [CompleteWord("--no-field-name")]
        word = self._current_word(document)
        yield from self._args_or_opts(word.text, self._paths, opts)

    def _clipboard(self, document):
        opts = [
            CompleteWord(
                "--clear-after", "seconds after which clipboard will be cleared"
            ),
            CompleteWord("--no-clear", "don't clear clipboard after copy"),
        ]

        word = self._current_word(document)

        text_before = document.text_before_cursor
        count_args = len(
            [
                w
                for w in get_words(text_before)
                if not w.text.startswith("-") and not w.has_errors
            ]
        )

        if count_args <= 1:
            completions = self._paths
        elif count_args == 2:
            completions = [CompleteWord("username"), CompleteWord("password")]
        else:
            completions = []

        yield from self._args_or_opts(word.text, completions, opts)

    def _autotype(self, document):
        opts = [
            CompleteWord("--default", "change default sequence for entries"),
            CompleteWord("--sequence", "override sequence"),
            CompleteWord("--force", "force auto-type even when disabled"),
            CompleteWord("--delay", "delay between keypresses"),
            CompleteWord("--backend", "force backend program for typing"),
            CompleteWord("--backend-command", "run a command to detect backend"),
        ]
        word = self._current_word(document)
        yield from self._args_or_opts(word.text, self._paths, opts)

    def _add(self, document):
        opts = [
            CompleteWord("--username", "username"),
            CompleteWord("--password", "password"),
            CompleteWord("--url", "URL"),
            CompleteWord("--note", "one line in notes"),
            CompleteWord("--autotype-sequence", "key sequence"),
            CompleteWord("--property", "custom property in form of name=val"),
            CompleteWord("--generate-password", "generate password interactively"),
            CompleteWord(
                "--generate-password-no-confirm", "generate password non-interactively"
            ),
            CompleteWord("--letters", "generate with letters"),
            CompleteWord("--digits", "generate with digits"),
            CompleteWord("--punctuation", "generate with punctuation"),
            CompleteWord("--logograms", "generate with logograms"),
            CompleteWord("--characters", "list of characters for password"),
            CompleteWord("--length", "password length"),
        ]
        word = self._current_word(document)
        yield from self._args_or_opts(word.text, self._groups_with_slash, opts)

    def _edit(self, document):
        opts = [
            CompleteWord("--username", "username"),
            CompleteWord("--password", "password"),
            CompleteWord("--askpass", "ask for password"),
            CompleteWord("--url", "URL"),
            CompleteWord("--delete-note", "delete note"),
            CompleteWord("--note", "add a line in notes"),
            CompleteWord("--autotype-sequence", "key sequence"),
            CompleteWord("--property", "custom property in form of name=val"),
            CompleteWord("--generate-password", "generate password interactively"),
            CompleteWord(
                "--generate-password-no-confirm", "generate password non-interactively"
            ),
            CompleteWord("--letters", "generate with letters"),
            CompleteWord("--digits", "generate with digits"),
            CompleteWord("--punctuation", "generate with punctuation"),
            CompleteWord("--logograms", "generate with logograms"),
            CompleteWord("--characters", "list of characters for password"),
            CompleteWord("--length", "password length"),
        ]
        word = self._current_word(document)
        yield from self._args_or_opts(word.text, self._paths, opts)

    def _delete(self, document):
        opts = [CompleteWord("--recursive", "delete groups recursively")]
        word = self._current_word(document)
        completions = self._paths + self._groups_with_slash
        yield from self._args_or_opts(word.text, completions, opts)

    def _move(self, document):
        word = self._current_word(document)

        if word.index == 1:
            completions = self._paths
        elif word.index == 2:
            completions = self._groups
        else:
            completions = []

        yield from self._complete_words(word.text, completions)

    def _ls(self, document):
        word = self._current_word(document)
        yield from self._complete_words(word.text, self._groups)

    def _help(self, document):
        word = self._current_word(document).text
        for command in self._commands:
            if command.startswith(word):
                yield Completion(command, -len(word))

    def _open(self, document):
        yield from self._filepath(document)

    def _args_or_opts(self, to_complete, args, opts):
        completions = sorted(opts) if to_complete.startswith("-") else sorted(args)
        yield from self._complete_words(to_complete, completions)

    def _complete_words(self, to_complete, complete_words):
        position = -len(to_complete)
        to_complete = unquote(to_complete)

        for cw in complete_words:
            if cw.word.startswith(to_complete):
                cw_q = quote(cw.word)
                yield Completion(cw_q, position, display=cw.word, display_meta=cw.meta)

    def _filepath(self, document):
        word = self._current_word(document).text
        position = -len(word)
        word = unquote(word)

        home = os.path.expanduser("~")
        tilde_repl = word.startswith("~/")
        for compl in glob.iglob("{}*".format(os.path.expanduser(word))):
            meta = None
            if os.path.isfile(compl):
                meta = "file"
            elif os.path.isdir(compl):
                meta = "dir"

            if tilde_repl:
                compl = compl.replace(home, "~")

            compl_q = quote(compl)
            if meta == "dir":
                compl_q = compl_q.rstrip("'")

            yield Completion(compl_q, position, display=compl, display_meta=meta)

    def _current_word(self, document):
        text_before = document.text_before_cursor
        words = list(get_words(text_before))
        if words:
            last = words[-1]

            # When there's a whitespace* after the last word, it means that
            # cursor is after the last word. We'll report it as an empty word.
            # This way, the caller gets correct word index. For example:
            #
            #   > move 'first arg' |
            #
            # should return index=2, enabling a different list of completions
            # for the second argument.
            #
            #   *: we check only for space though
            if not last.has_errors and text_before.endswith(" "):
                return Word(len(words), "", False)

            # Normally get_words() works in POSIX mode, which returns unquoted
            # strings. We make an exception for the last word to enable correct
            # completion of strings like >> move 'foo' <<. Otherwise, the
            # completion's position would be shifted and we'd end up with sth
            # like >> move 'ffoo/bar' <<
            if not last.has_errors and any(text_before.endswith(ch) for ch in _QUOTES):
                return Word(last.index, f"'{last.text}'", False)

            # Otherwise, just return the last word.
            else:
                return last
        return Word(0, "", False)

    @property
    def _paths(self):
        if self._kp.locked:
            return []
        return [CompleteWord(p, "entry") for p in self._kp.paths]

    @property
    def _groups(self):
        if self._kp.locked:
            return []
        return [CompleteWord(g, "group") for g in self._kp.groups]

    @property
    def _groups_with_slash(self):
        if self._kp.locked:
            return []
        return [CompleteWord(f"{g}/", "group") for g in self._kp.groups]


def get_words(text):
    lex = shlex.shlex(text, posix=True)
    lex.whitespace_split = True

    startpos = lex.instream.tell()
    i = 0
    while True:
        try:
            word = lex.get_token()
            has_errors = False
        except ValueError:
            word = text[startpos:]
            has_errors = True

        if word is None or startpos >= len(text):
            break

        yield Word(i, word, has_errors)

        startpos = lex.instream.tell()
        i += 1


def unquote(text):
    text = text.strip(_QUOTES).replace("\\", "")
    return text


def quote(text):
    if (" " in text or "\\" in text) and not (
        text.startswith("'") and text.endswith("'")
    ):
        return shlex.quote(text)
    return text
