# -*- coding: utf-8 -*-
#
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
    fabulous.text
    ~~~~~~~~~~~~~

    The text module makes it possible to print TrueType text to the terminal.
    This functionality is available on the command line::

        jart@compy:~$ fabulous-text --help
        jart@compy:~$ fabulous-text --skew=5 --shadow 'Fabulous!'
        jart@compy:~$ python -m fabulous.text --help

    Or as a Python library:

    .. code-block:: python

        from fabulous import text
        print text.Text("Fabulous!", color='#0099ff', shadow=True, skew=5)

    To make things simple, Fabulous bundles the following Google Noto Fonts
    which look good and are guaranteed to work no matter what:

    - NotoSans-Bold
    - NotoEmoji-Regular

    For other fonts, Fabulous will do its best to figure out where they are
    stored. If Fabulous has trouble finding your font, try using an absolute
    path *with* the extension. It's also possible to put the font in the
    ``~/.fonts`` directory and then running ``fc-cache -fv ~/.fonts``.

    You can run ``fabulous-text --list`` to see what fonts are available.

"""

from __future__ import print_function

import os
import sys

from fabulous import utils, image, grapefruit
from fabulous.compatibility import printy

try:
    unicode = unicode
except NameError:
    unicode = str
    basestring = (str, bytes)


class Text(image.Image):
    u"""Renders TrueType Text to Terminal

    I'm a sub-class of :class:`fabulous.image.Image`.  My job is
    limited to simply getting things ready.  I do this by:

    - Turning your text into an RGB-Alpha bitmap image using
      :mod:`PIL`

    - Applying way cool effects (if you choose to enable them)

    For example::

        >>> assert Text("Fabulous", shadow=True, skew=5)

        >>> txt = Text("lorem ipsum", font="NotoSans-Bold")
        >>> len(str(txt)) > 0
        True
        >>> txt = Text(u"😃", font="NotoSans-Bold")
        >>> len(str(txt)) > 0
        True

    :param text:   The text you want to display as a string.

    :param fsize:  The font size in points.  This obviously end up
                   looking much larger because in fabulous a single
                   character is treated as one horizontal pixel and two
                   vertical pixels.

    :param color:  The color (specified as you would in HTML/CSS) of
                   your text.  For example Red could be specified as
                   follows: ``red``, ``#00F`` or ``#0000FF``.

    :param shadow: If true, render a simple drop-shadow beneath text.
                   The Fabulous logo uses this feature.

    :param skew:   Skew size in pixels.  This applies an affine
                   transform to shift the top-most pixels to the right.
                   The Fabulous logo uses a five pixel skew.

    :param font:   The TrueType font you want.  If this is not an
                   absolute path, Fabulous will search for your font by
                   globbing the specified name in various directories.
    """

    def __init__(self, text, fsize=23, color="#0099ff", shadow=False,
                 skew=None, font='NotoSans-Bold'):
        raise NotImplementedError


class FontNotFound(ValueError):
    """I get raised when the font-searching hueristics fail

    This class extends the standard :exc:`ValueError` exception so you
    don't have to import me if you don't want to.
    """


def resolve_font(name):
    """Turns font names into absolute filenames

    This is case sensitive. The extension should be omitted.

    For example::

        >>> path = resolve_font('NotoSans-Bold')

        >>> fontdir = os.path.join(os.path.dirname(__file__), 'fonts')
        >>> noto_path = os.path.join(fontdir, 'NotoSans-Bold.ttf')
        >>> noto_path = os.path.abspath(noto_path)
        >>> assert path == noto_path

    Absolute paths are allowed::

        >>> resolve_font(noto_path) == noto_path
        True

    Raises :exc:`FontNotFound` on failure::

        >>> try:
        ...     resolve_font('blahahaha')
        ...     assert False
        ... except FontNotFound:
        ...     pass

    """
    pass

font_roots = [
    '/usr/share/fonts/truetype',                # where ubuntu puts fonts
    '/usr/share/fonts',                         # where fedora puts fonts
    os.path.expanduser('~/.local/share/fonts'), # custom user fonts
    os.path.expanduser('~/.fonts'),             # custom user fonts
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'fonts')),
]

@utils.memoize
def get_font_files():
    """Returns a list of all font files we could find

    Returned as a list of dir/files tuples::

        get_font_files() -> {'FontName': '/abs/FontName.ttf', ...]

    For example::

        >>> fonts = get_font_files()
        >>> 'NotoSans-Bold' in fonts
        True
        >>> fonts['NotoSans-Bold'].endswith('/NotoSans-Bold.ttf')
        True

    """
    pass


def main():
    """Main function for :command:`fabulous-text`."""
    pass


if __name__ == '__main__':
    main()
