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
    fabulous.debug
    ~~~~~~~~~~~~~~

    The debug module provides the ability to print images as ASCII. It isn't a
    good ASCII representation like cacalib. This module is mostly intended for
    debugging purposes (hence the name.)

"""

from __future__ import print_function

import sys
import itertools

from fabulous import image


class DebugImage(image.Image):
    """Visualize optimization techniques used by :class:`Image`
    """

    def reduce(self, colors):
        pass


def main():
    """I provide a command-line interface for this module
    """
    pass


if __name__ == '__main__':
    main()
