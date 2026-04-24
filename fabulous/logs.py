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
    fabulous.logs
    ~~~~~~~~~~~~~

    Utilities for transient logging.

    This is very useful tool for monitoring what your Python scripts are doing.
    It allows you to have full verbosity without drowning out important error
    messages:

    .. code-block:: python

        import time, logging
        from fabulous import logs
        logs.basicConfig(level='WARNING')

        for n in range(20):
            logging.debug("verbose stuff you don't care about")
            time.sleep(0.1)
        logging.warning("something bad happened!")
        for n in range(20):
            logging.debug("verbose stuff you don't care about")
            time.sleep(0.1)

"""

import sys
import logging

from fabulous import utils


class TransientStreamHandler(logging.StreamHandler):
    """Standard Python logging Handler for Transient Console Logging

    Logging transiently means that verbose logging messages like DEBUG
    will only appear on the last line of your terminal for a short
    period of time and important messages like WARNING will scroll
    like normal text.

    This allows you to log lots of messages without the important
    stuff getting drowned out.

    This module integrates with the standard Python logging module.
    """

    def __init__(self, strm=sys.stderr, level=logging.WARNING):
        raise NotImplementedError

    def close(self):
        pass

    def write(self, data):
        pass

    def transient_write(self, data):
        pass

    def emit(self, record):
        pass


def basicConfig(level=logging.WARNING, transient_level=logging.NOTSET):
    """Shortcut for setting up transient logging

    I am a replica of ``logging.basicConfig`` which installs a
    transient logging handler to stderr.
    """
    pass
