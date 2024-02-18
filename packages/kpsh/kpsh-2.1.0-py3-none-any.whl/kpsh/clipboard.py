# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2023 Michał Góral.

import shutil
import subprocess

from kpsh.environment import detect_environment, OS, Environment


def _wl_copy(text: str):
    subprocess.run(["wl-copy", text], check=True)


def _wl_copy_clear():
    subprocess.run(["wl-copy", "-c"], check=True)


def _xclip(text: str):
    subprocess.run(
        ["xclip", "-i", "-selection", "clipboard"], text=True, input=text, check=True
    )


def _xclip_clear():
    subprocess.run(
        ["xclip", "-i", "-selection", "clipboard"], text=True, input="", check=True
    )


def expect_prog(prog: str):
    if shutil.which(prog) is None:
        raise OSError(f"{prog} not found")


def _get_programs(os: OS, environment: Environment):
    if os is OS.Unknown or environment is Environment.Unknown:
        raise OSError("unsupported environment")

    if os == OS.Linux:
        if environment == Environment.Wayland:
            expect_prog("wl-copy")
            return _wl_copy, _wl_copy_clear
        elif environment == Environment.X11:
            expect_prog("xclip")
            return _xclip, _xclip_clear

    raise OSError(f"unsupported clipboard environment: {os}, {environment}")


def copy_to_clipboard(text: str, clear_after=0):
    os, environment = detect_environment()
    ccopy, _ = _get_programs(os, environment)
    ccopy(text)


def clear_clipboard():
    os, environment = detect_environment()
    _, cclear = _get_programs(os, environment)
    cclear()
