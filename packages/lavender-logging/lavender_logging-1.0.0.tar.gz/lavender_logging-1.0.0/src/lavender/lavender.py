import logging
import os
import sys
from typing import Dict, Optional, TextIO

"""
MIT License

Copyright (c) 2023 NimajnebEC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

ENVIRON_CONFIG_PREFIX = "LOG_"


def setup(
    *,
    level: int = logging.INFO,
    logger: logging.Logger = logging.getLogger(),
    handler: logging.Handler = logging.StreamHandler(),
    formatter: Optional[logging.Formatter] = None,
    filter_config: Dict[str, int] = {},
    environ_config: bool = True,
):
    """Set up Lavender with basic settings.

    Parameters
    ----------
    level : `int`, optional
        The default level to filter messages, by default `logging.INFO`
    logger : `logging.Logger`, optional
        The logger to setup Lavender on, by default the root logger is used
    handler : `logging.Handler`, optional
        The logging handler to use, by default `logging.StreamHandler()`
    formatter : `logging.Formatter`, optional
        The formatter used by the logger, by default Lavender will pick one for you
    filter_config : `Dict[str, int]`, optional
        Initial filter patterns, by default no specific filters are specified
    environ_config : `bool`, optional
        Wether filter patterns should be loaded from environ, by default `True`
    """
    if formatter is not None:
        handler.setFormatter(formatter)
    elif isinstance(handler, logging.StreamHandler) and stream_supports_colour(handler.stream):
        handler.setFormatter(ColourFormatter())
    else:
        handler.setFormatter(
            logging.Formatter(
                "[{asctime}] [{levelname:<8}] {name}: {message}",
                "%Y-%m-%d %H:%M:%S",
                style="{",
            )
        )

    # Load configurations
    if environ_config:
        for key, value in logging._nameToLevel.items():
            key = ENVIRON_CONFIG_PREFIX + key
            if key in os.environ:
                patterns = os.environ[key].split(os.pathsep)
                for pattern in patterns:
                    filter_config[pattern] = value

    filters = {PackagePattern(k): v for k, v in filter_config.items()}
    handler.addFilter(CompositeLevelFilter(level, filters))

    logger.addHandler(handler)
    logger.setLevel(0)


class PackagePattern:
    def __init__(self, pattern: str) -> None:
        self._cache: Dict[str, Optional[float]] = {}

        split = pattern.strip(".").split(".")

        self._wildcard = split[-1] == "*"
        if self._wildcard:
            split.pop(-1)

        self._segments = len(split)
        self._pattern = ".".join(split)
        self._length = len(self._pattern)

    def match(self, package: str) -> Optional[float]:
        if package not in self._cache:
            self._cache[package] = self._match(package)

        return self._cache[package]

    def _match(self, package: str) -> Optional[float]:
        if self._wildcard:
            if package.startswith(self._pattern):
                inferred = len(package[self._length + 1 :].split(".")) + 1
                total = inferred + self._segments
                return inferred / total
            return None
        else:
            return 0 if package == self._pattern else None

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, PackagePattern)
            and self._pattern == other._pattern
            and self._wildcard == other._wildcard
        )

    def __hash__(self) -> int:
        return (hash(self._pattern) << 1) + self._wildcard

    def __repr__(self) -> str:
        full = self._pattern + (".*" if self._wildcard else "")
        return f"<{type(self).__name__} '{full}'>"


class CompositeLevelFilter(logging.Filter):
    def __init__(self, default: int, levels: Dict[PackagePattern, int] = {}) -> None:
        self._cache: Dict[str, int] = {}
        self._default = default
        self._levels = levels

    def filter(self, record: logging.LogRecord) -> bool:
        if record.name not in self._cache:
            self._cache[record.name] = self.level_for(record.name)
        return record.levelno >= self._cache[record.name]

    def level_for(self, name: str) -> int:
        best_level = self._default
        best_ratio = 2

        for pattern, level in self._levels.items():
            ratio = pattern.match(name)
            if ratio is not None and ratio < best_ratio:
                best_ratio = ratio
                best_level = level

        return best_level

    def set_default(self, level: int) -> None:
        self._default = level
        self._cache.clear()

    def set_level(self, pattern: PackagePattern, level: int) -> None:
        self._levels[pattern] = level
        self._cache.clear()


"""
The MIT License (MIT)

Copyright (c) 2015-present Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""


def is_docker() -> bool:
    path = "/proc/self/cgroup"
    return os.path.exists("/.dockerenv") or (
        os.path.isfile(path) and any("docker" in line for line in open(path))
    )


def stream_supports_colour(stream: TextIO) -> bool:
    is_a_tty = hasattr(stream, "isatty") and stream.isatty()

    # Pycharm and Vscode support colour in their inbuilt editors
    if "PYCHARM_HOSTED" in os.environ or os.environ.get("TERM_PROGRAM") == "vscode":
        return is_a_tty

    if sys.platform != "win32":
        # Docker does not consistently have a tty attached to it
        return is_a_tty or is_docker()

    # ANSICON checks for things like ConEmu
    # WT_SESSION checks if this is Windows Terminal
    return is_a_tty and ("ANSICON" in os.environ or "WT_SESSION" in os.environ)


class ColourFormatter(logging.Formatter):
    # ANSI codes are a bit weird to decipher if you're unfamiliar with them, so here's a refresher
    # It starts off with a format like \x1b[XXXm where XXX is a semicolon separated list of commands
    # The important ones here relate to colour.
    # 30-37 are black, red, green, yellow, blue, magenta, cyan and white in that order
    # 40-47 are the same except for the background
    # 90-97 are the same but "bright" foreground
    # 100-107 are the same as the bright ones but for the background.
    # 1 means bold, 2 means dim, 0 means reset, and 4 means underline.

    LEVEL_COLOURS = [
        (logging.DEBUG, "\x1b[40;1m"),
        (logging.INFO, "\x1b[34;1m"),
        (logging.WARNING, "\x1b[33;1m"),
        (logging.ERROR, "\x1b[31m"),
        (logging.CRITICAL, "\x1b[41m"),
    ]

    FORMATS = {
        level: logging.Formatter(
            f"\x1b[30;1m%(asctime)s\x1b[0m {colour}%(levelname)-8s\x1b[0m \x1b[35m%(name)s\x1b[0m %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )
        for level, colour in LEVEL_COLOURS
    }

    def format(self, record):
        formatter = self.FORMATS.get(record.levelno)
        if formatter is None:
            formatter = self.FORMATS[logging.DEBUG]

        # Override the traceback to always print in red
        if record.exc_info:
            text = formatter.formatException(record.exc_info)
            record.exc_text = f"\x1b[31m{text}\x1b[0m"

        output = formatter.format(record)

        # Remove the cache layer
        record.exc_text = None
        return output
