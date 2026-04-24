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
    fabulous.gotham
    ~~~~~~~~~~~~~~~

    This is a gimmick feature that generates silly gothic poetry.

    This uses a simple mad lib algorithm. It has no concept of meter or rhyme.
    If you want a *proper* poetry generator, check out poemy2_ which uses markov
    chains and isledict. It's written by the same author as Fabulous.

    This module can be run as a command line tool::

        jart@compy:~$ fabulous-gotham
        jart@compy:~$ python -m fabulous.gotham

    .. _poemy2: https://github.com/jart/poemy2

"""

from __future__ import print_function

import sys
import random
import itertools

try:
  next
except NameError:
  next = lambda x: x.next()


them = ['angels', 'mourners', 'shadows', 'storm clouds', 'memories', 'condemned',
        'hand of Heaven', 'stroke of death', 'damned', 'witches', 'corpses']
them_verb = ['follow', 'hover close', 'approach', 'loom', 'taunt',
             'laugh', 'surround', 'compell', 'scour']
adj = ['cold', 'dead', 'dark', 'frozen', 'angry', 'ghastly', 'unholy', 'cunning', 'deep',
       'morose', 'maligned', 'rotting', 'sickly']
me_part = ['neck', 'heart', 'head', 'eyes', 'soul', 'blood', 'essence', 'wisdom']
feeling = ['pain', 'horror', 'frenzy', 'agony', 'numbness', 'fear', 'love',
           'terror', 'madness', 'torment', 'bitterness', 'misery']
angst = ['care', 'understand', 'question']
me_verb = ['flee', 'dance', 'flail madly', 'fall limply', 'hang my head', 'try to run',
           'cry out', 'call your name', 'beg forgiveness', 'bleed', 'tremble', 'hear']
action = ['sever', 'crush', 'mutilate', 'slay', 'wound', 'smite', 'drip',
          'melt', 'cast', 'mourn', 'avenge']
place = ['the witching hour', 'the gates of hell', 'the door', 'the path', 'death',
         'my doom', 'oblivion', 'the end of life', 'Hell', 'nothingness', 'purgatory',
         'void', 'earth', 'tomb', 'broken ground', 'barren land', 'swirling dust']


def lorem_gotham():
    """Cheesy Gothic Poetry Generator

    Uses Python generators to yield eternal angst.

    When you need to generate random verbiage to test your code or
    typographic design, let's face it... Lorem Ipsum and "the quick
    brown fox" are old and boring!

    What you need is something with *flavor*, the kind of thing a
    depressed teenager with a lot of black makeup would write.
    """
    pass


def lorem_gotham_title():
    """Names your poem
    """
    pass


def main():
    """I provide a command-line interface for this module
    """
    pass


if __name__ == '__main__':
    main()
