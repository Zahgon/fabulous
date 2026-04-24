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
    fabulous.rlcomplete
    ~~~~~~~~~~~~~~~~~~~

    Readline related stuff.
"""

import os

class Completer(object):
    """A base class for completers.
    
    Child classes should implement the completelist method.
    """
    text = None
    
    delims = '\t\n'
    
    def __init__(self):
        pass
    
    def complete(self, text, state):
        """The actual completion method
        
        This method is not meant to be overridden. Override the
        completelist method instead. It will make your life much easier.
        
        For more detail see documentation for readline.set_completer
        """
        pass

    def completelist(self, text):
        """Returns a list.
        
        The list contains a series of strings which are the suggestions
        for the given string ``text``. It is valid to have no suggestions
        (empty list returned).
        """
        pass

class ListCompleter(Completer):
    """A class that does completion based on a predefined list.
    """
    
    def __init__(self, words, ignorecase):
        raise NotImplementedError
    
    def completelist(self,text):
        pass


class PathCompleter(Completer):
    """Does completion based on file paths. """
    
    def buildpath(self, base, *paths):
        pass
    
    @staticmethod
    def matchuserhome(prefix):
        """To find matches that start with prefix.
        
        For example, if prefix = '~user' this
        returns list of possible matches in form of ['~userspam','~usereggs'] etc.
        
        matchuserdir('~') returns all users
        """
        pass
        
    
    def completelist(self, text):
        """Return a list of potential matches for completion
        
        n.b. you want to complete to a file in the current working directory
        that starts with a ~, use ./~ when typing in. Paths that start with
        ~ are magical and specify users' home paths
        """
        pass
