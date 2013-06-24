#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 6/18/2013, updated 6/18/2013
#
""" Utilities for dividing a sequence into multiple chunks.

TODO/TOREAD:
http://code.activestate.com/recipes/542194/
http://code.activestate.com/recipes/521877/
"""
__all__ = [
    'chunked_by_partsize',
    'chunked_by_numparts',
]
print('Executing %s' %  __file__)

import os, sys, time, random

def _chunked_by_partsize_numparts (seq, partsize, numparts, shuffle):
    if shuffle:
        seq = list(seq)  # copy
        random.shuffle(seq, random.random) # in-place shuffling
    parts = [seq[i*partsize: (i+1)*partsize] for i in range(numparts)]
    if partsize * numparts < len(seq):
        for i, x in enumerate(seq[partsize*numparts:]):
            parts[i].append(x)
    return parts

def chunked_by_partsize (seq, partsize, shuffle=False):
    """ Divides a sequence into chunks, each of which have almost equal size
        specified in the 'partsize' argument.
    """
    seqlen = len(seq)
    numparts = seqlen // partsize
    if numparts * partsize < seqlen:
        numparts += 1
    parts = _chunked_by_partsize_numparts (seq, partsize, numparts, shuffle)
    return parts

def chunked_by_numparts (seq, numparts, shuffle=False):
    """ Divides a sequence into a specified number of equal-size parts.
    """
    seqlen = len(seq)
    partsize = seqlen // numparts
    parts = _chunked_by_partsize_numparts (seq, partsize, numparts, shuffle)
    return parts


if __name__ == '__main__':
    t0 = time.time()
    print('Done. Time elapsed: %.2f.' % (time.time() - t0))
