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

import logging
import itertools

from fabulous.logs import *
from fabulous.gotham import *
from fabulous.color import *

try:
  next
except NameError:
  next = lambda x: x.next()


logger = logging.getLogger('fabulous')


def luv():
    raise NotImplementedError


def bad_things():
    raise NotImplementedError


def test_transientlogger():
    raise NotImplementedError


def test_transientlogger2():
    raise NotImplementedError


if __name__ == '__main__':
    basicConfig(level=logging.WARNING)
    logging.warning("RUNNING TEST: test_transientlogger()")
    test_transientlogger()
    logging.warning("RUNNING TEST: test_transientlogger2()")
    test_transientlogger2()
