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
    fabulous.rotating_cube
    ~~~~~~~~~~~~~~~~~~~~~~

    Command for animating a wireframe rotating cube in the terminal.

"""

from __future__ import with_statement
from __future__ import division

import sys
import time
from math import cos, sin, pi

from fabulous import color, utils


class Frame(object):
    """Canvas object for drawing a frame to be printed
    """

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, type_, value, traceback):
        raise NotImplementedError

    def __setitem__(self, p, c):
        raise NotImplementedError

    def line(self, x0, y0, x1, y1, c='*'):
        r"""Draws a line

        Who would have thought this would be so complicated?  Thanks
        again Wikipedia_ <3

        .. _Wikipedia: http://en.wikipedia.org/wiki/Bresenham's_line_algorithm
        """
        pass

    def render(self):
        pass


def rotating_cube(degree_change=3, frame_rate=3):
    """Rotating cube program

    How it works:

      1. Create two imaginary ellipses
      2. Sized to fit in the top third and bottom third of screen
      3. Create four imaginary points on each ellipse
      4. Make those points the top and bottom corners of your cube
      5. Connect the lines and render
      6. Rotate the points on the ellipses and repeat

    """
    pass


def ellipse_point(degrees, width, height):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
