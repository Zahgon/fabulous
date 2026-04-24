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
    fabulous.widget
    ~~~~~~~~~~~~~~~

    Widget library using terminate.

"""

import os
import math
from datetime import datetime
# import textwrap
from term import stdout, display

class ProgressBar(object):
    """A 3-line progress bar, which looks like::
                                title
        39% [================>----------------------------]
                               message
    
        p = ProgressBar('spam') # create bar
        p.update(0, 'starting spam') # start printing it out
        p.update(50, 'spam almost ready') # progress
        p.update(100, 'spam complete')
    """
    # content, length
    TITLE_FORMAT = {'text':display('bright','cyan') + '%s' + display('default'),
           'length':0,
           'padding':0 }
    BAR_FORMAT = {'text':' %3d%% ' + '[%s'+display('dim')+'%s'+display('default')+']',
           'length':8,
           'padding':2 }
    MESSAGE_FORMAT = {'text': '%s',
           'length': 0,
           'padding': 0 }
        
    def __init__(self, title = None):
        """
        """
        raise NotImplementedError
    
    def set_title(self, title = None):
        """
        """
        pass
            #lines = [(padding + line + padding) for line in textwrap.wrap(
            #          text, self.width - (self.TITLE_FORMAT['padding']*2),
            #          replace_whitespace=False)]
            #self.title = os.linesep.split(
            #          self.TITLE_FORMAT['text'] % os.linesep.join(lines))
    
    def get_title(self):
        """
        """
        pass
    
    def get_bar(self, percent):
        """
        """
        pass
    
    def set_message(self, message = None):
        """
        """
        pass
    
    def get_message(self):
        """returns None or string"""
        pass
    
    def update(self, percent, message = None, test = False):
        """
        """
        pass
    
    def clear(self):
        """
        """
        pass

class TimedProgressBar(ProgressBar):
    """A 3-line progress bar, which looks like::
                                      title
        39% [================>----------------------------] ETA mm:ss
                                     message
    
        p = ProgressBar('spam') # create bar
        p.update(0, 'starting spam') # start printing it out
        p.update(50, 'spam almost ready') # progress
        p.update(100, 'spam complete')
    """
    
    BAR_FORMAT = {'text':' %3d%% ' + '[%s'+display('dim')+'%s'+display('default')+']',
           'length':13,
           'padding':2 }
    ' ETA 12:23'
    
    # what fraction of percent it acurate too
    precision = 100
    
    def __init__(self, title = None):
        raise NotImplementedError
    
    def get_bar(self, percent):
        pass

class Spinner(object):
    
    spinners=['/','-','\\','|',]
    
    def __init__(self):
        raise NotImplementedError
    
    def spin(self):
        pass
        
    def clear(self):
        pass
