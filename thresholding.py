#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 04/20/2013, updated 06/25/2013
#
""" Deciding thresholds on a sequence.
"""
__all__ = [
    'natural_cutoff',
]
print('Executing %s' %  __file__)

import os, sys, time


def natural_cutoff (sequence, lo, hi):
    """
    The adaptive/"natural" cutoff problem: given a sequence of values each in
    [0.0, 1.0], and a pre-specified range [lo,hi] (0<lo<hi<1), how to find a
    'natural' threshold/cutoff within [lo, hi].

    Our proposed method is as follows.

    Sort val_1 <= val_2 <= ... <= val_n.
    Define gap delta_i = val_{i+1} - val_i, for 1 <= i <= n-1

    A "natural" threshold should be placed between val_m and val_{m+1}
    (i.e. set threshold=val_m) such that delta_m is the first delta_i
    satisfying either of these conditions:

    a. delta_m > 0.1
    b. (delta_m > 0.05) and (delta_m > 2* delta_{m-1})

    If such threshold does not exist within [lo,hi], then set threshold=lo.


    For example, let us assume lo=0.2, hi=0.5.

    E.g. sequence = [0.28, 0.40, 0.50, 0.65...]
    delta_sequence   = [0.12, 0.10, 0.15, ...]
    Cut on delta_m = 0.12 (i.e. between 0.28 and 0.40)
    because 0.12 is the first gap larger than 0.1.
    So we choose threshold=0.28.

    E.g. sequence = [0.1, 0.17, 0.21, 0.30, 0.51, ...]
    delta_sequence  = [0.07, 0.04, 0.09, 0.21, ...]
    Cut on delta_m = 0.09 (i.e. between 0.21 and 0.30) because 0.09 > 0.05
    and it is at least twice of the previous gap (i.e. 0.09 > 2*0.04).
    So we choose threshold=0.21, which also falls in [lo,hi].

    E.g. sequence = [0.1, 0.17, 0.21, 0.28, 0.37, 0.45, 0.51, ...]
    delta_sequence  = [0.07, 0.04, 0.07, 0.09, 0.08, 0.06, ...]
    In this case, no delta_m satisfies either condition a or condition b,
    so we just set threshold=lo=0.2.

    """
    assert 0 <= lo <= hi <= 1
    seq = sorted(sequence) # seq_i for i = 0, 1, ..., n-1
    n = len(seq)

    # gap_i = seq_{i+1} - seq_i for i = 0, 1, ..., n-2
    #gap = [y - x for x, y in zip(seq, seq[1:])]

    # Preset cutoff=lo, in case no cutoff is found
    cutoff = lo

    # i = 0, 1, ..., n-2
    for i in xrange(n-1):

        # Break if interval [seq_i, seq_{i+1}] has already gone beyond hi
        if seq[i] > hi:
            break

        # Continue if interval [seq_i, seq_{i+1}] hasn't reached lo yet
        elif seq[i+1] < lo:
            continue

        # Now we have one of the following cases:
        #     lo <= seq_i <= seq_{i+1} <= hi
        #     lo <= seq_i <= hi <= seq_{i+1}
        #     seq_i <= lo <= hi <= seq_{i+1}
        #     seq_i <= lo <= seq_{i+1} <= hi
        # Let us test whether we should cut on some value in [seq_i, seq_{i+1}]
        gap_i = seq[i+1] - seq[i]
        if gap_i > 0.1:
            cutoff = max(lo, seq[i])
            break
        elif gap_i > 0.05 and i > 0:
            gap_i_minus1 = seq[i] - seq[i-1]
            if gap_i > 2* gap_i_minus1:
                cutoff = max(lo, seq[i])
                break

    return cutoff


if __name__ == '__main__':
    t0 = time.time()
    print('Done. Time elapsed: %.2f.' % (time.time() - t0))
