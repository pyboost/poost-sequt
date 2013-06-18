# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 6/18/2013, updated 6/18/2013
#
""" Additional utilities and helper functions for Python sequence types,
    e.g. list, tuple, str ..., or any other ojects obey the sequence protocol
    in Python's abstract objects layer.
"""
from __future__ import absolute_import

__version__ = '0.1.1'

import sys
if sys.version_info[:2] < (2, 6):
    raise ImportError("CPython 2.6.x or above is required (%d.%d detected)."
                      % sys.version_info[:2])

from .chunking import *

del sys, absolute_import
