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

from __future__ import with_statement

import time
import curses


class Canvas(object):
    def __init__(self, encoding='UTF-8'):
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, type_, value, traceback):
        raise NotImplementedError

    def __setitem__(self, xy, val):
        raise NotImplementedError


if __name__ == '__main__':
    import locale
    locale.setlocale(locale.LC_ALL, '')
    encoding = locale.getpreferredencoding()
    with Canvas(encoding=encoding) as canvas:
        canvas[5, 5] = 'Y'
        canvas.win.refresh()
        time.sleep(5.0)
