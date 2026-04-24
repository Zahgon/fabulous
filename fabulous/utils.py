# Copyright 2016 The Fabulous Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
    fabulous.utils
    ~~~~~~~~~~~~~~

    Miscellaneous utilities for Fabulous.

"""

import os
import sys
import fcntl
import struct
import termios
import textwrap
import functools

from fabulous import grapefruit


def memoize(function):
    """A very simple memoize decorator to optimize pure-ish functions

    Don't use this unless you've examined the code and see the
    potential risks.
    """
    pass


class TerminalInfo(object):
    """Quick and easy access to some terminal information

    I'll tell you the terminal width/height and it's background color.

    You don't need to use me directly.  Just access the global
    :data:`term` instance::

        >>> assert term.width > 0
        >>> assert term.height > 0

    It's important to know the background color when rendering PNG
    images with semi-transparency.  Because there's no way to detect
    this, black will be the default::

        >>> term.bgcolor
        (0.0, 0.0, 0.0, 1.0)
        >>> from fabulous import grapefruit
        >>> isinstance(term.bgcolor, grapefruit.Color)
        True

    If you use a white terminal, you'll need to manually change this::

        >>> term.bgcolor = 'white'
        >>> term.bgcolor
        (1.0, 1.0, 1.0, 1.0)
        >>> term.bgcolor = grapefruit.Color.NewFromRgb(0.0, 0.0, 0.0, 1.0)
        >>> term.bgcolor
        (0.0, 0.0, 0.0, 1.0)

    """

    def __init__(self, bgcolor='black'):
        raise NotImplementedError

    @property
    def termfd(self):
        """Returns file descriptor number of terminal

        This will look at all three standard i/o file descriptors and
        return whichever one is actually a TTY in case you're
        redirecting i/o through pipes.
        """
        pass

    @property
    def dimensions(self):
        """Returns terminal dimensions

        Don't save this information for long periods of time because
        the user might resize their terminal.

        :return: Returns ``(width, height)``.  If there's no terminal
                 to be found, we'll just return ``(79, 40)``.
        """
        pass

    @property
    def width(self):
        """Returns width of terminal in characters
        """
        pass

    @property
    def height(self):
        """Returns height of terminal in lines
        """
        pass

    def _get_bgcolor(self):
        pass

    def _set_bgcolor(self, color):
        pass

    bgcolor = property(_get_bgcolor, _set_bgcolor)


term = TerminalInfo()


def pil_check():
    """Check for PIL library, printing friendly error if not found

    We need PIL for the :mod:`fabulous.text` and :mod:`fabulous.image`
    modules to work.  Because PIL can be very tricky to install, it's
    not listed in the ``setup.py`` requirements list.
    """
    pass
