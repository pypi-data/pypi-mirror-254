# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2023 Michał Góral.

from enum import Enum
import os
import platform

class OS(Enum):
    Unknown = 0
    Linux = 1
    Windows = 2
    MacOS = 3


class Environment(Enum):
    Unknown = 0
    X11 = 1
    Wayland = 2


def detect_environment():
    if platform.system() == "Linux":
        if os.environ.get("WAYLAND_DISPLAY"):
            return OS.Linux, Environment.Wayland
        return OS.Linux, Environment.X11
    if platform.system() == "Windows":
        return OS.Windows, Environment.Unknown
    if platform.system() == "Darwin":
        return OS.MacOS, Environment.Unknown
    return OS.Unknown, Environment.Unknown
