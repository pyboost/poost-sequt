#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 06/27/2013, updated 06/27/2013
#
""" Deduplication: removing duplicated elements from a sequence.

    Reference:
    http://code.activestate.com/recipes/52560/
"""
__all__ = [
    'dedup',
]
print('Executing %s' %  __file__)

import os, sys, time

def dedup (seq):
    pass


if __name__ == '__main__':
    t0 = time.time()
    print('Done. Time elapsed: %.2f.' % (time.time() - t0))
