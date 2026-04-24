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
    fabulous.xterm256
    ~~~~~~~~~~~~~~~~~

    The xterm256 module provides support for the 256 colors supported by xterm
    as well as quantizing 24-bit RGB color to xterm color ids.

    Color quantization may perform slowly depending on whether or not Fabulous
    is able to compile ``~/.xterm256.so`` on the fly. This is a tiny library
    that makes color quantization go much faster. The pure Python version of the
    algorithm is really slow because it's implemented as a brute force nearest
    neighbor over Euclidean distance search. Although an O(1) version of this
    algorithm exists with slightly less correctness. Your humble author simply
    hasn't had the time to implement it in this library.

"""

import logging


CUBE_STEPS = [0x00, 0x5F, 0x87, 0xAF, 0xD7, 0xFF]
BASIC16 = ((0, 0, 0), (205, 0, 0), (0, 205, 0), (205, 205, 0),
           (0, 0, 238), (205, 0, 205), (0, 205, 205), (229, 229, 229),
           (127, 127, 127), (255, 0, 0), (0, 255, 0), (255, 255, 0),
           (92, 92, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255))


def xterm_to_rgb(xcolor):
    """Convert xterm Color ID to an RGB value

    All 256 values are precalculated and stored in :data:`COLOR_TABLE`
    """
    pass


COLOR_TABLE = [xterm_to_rgb(i) for i in range(256)]


def rgb_to_xterm(r, g, b):
    """Quantize RGB values to an xterm 256-color ID

    This works by envisioning the RGB values for all 256 xterm colors
    as 3D euclidean space and brute-force searching for the nearest
    neighbor.

    This is very slow.  If you're very lucky, :func:`compile_speedup`
    will replace this function automatically with routines in
    `_xterm256.c`.
    """
    pass


def compile_speedup():
    """Tries to compile/link the C version of this module

    Like it really makes a huge difference.  With a little bit of luck
    this should *just work* for you.

    You need:

    - Python >= 2.5 for ctypes library
    - gcc (``sudo apt-get install gcc``)

    """
    pass


try:
    (rgb_to_xterm, xterm_to_rgb) = compile_speedup()
except OSError:
    logging.debug("fabulous failed to compile xterm256 speedup code")
