# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 06/18/2013, updated 06/25/2013
#
""" Additional utilities and helper functions for Python sequence types,
    e.g. list, tuple, str ..., or any other ojects that obey the sequence
    protocol in Python's abstract objects layer.
"""
from __future__ import absolute_import

print('Executing %s' %  __file__)

import sys
if not (2, 6) <= sys.version_info < (3, ):
    raise ImportError("CPython 2.6.x or 2.7.x is required (%d.%d detected)."
                      % sys.version_info[:2])

from .chunking import *
from .thresholding import *

del sys, absolute_import

__version__ = '0.1.3-a1'

