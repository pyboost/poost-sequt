#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 6/18/2013, updated 6/18/2013
#
""" Unit tests for chunking.py
"""
print('Executing %s' %  __file__)

import unittest
import os, sys, time

import poost.sequtils as sequtils

class Test_chunking (unittest.TestCase):
    """
    """
    def setUp (self):
        self.seq1 = range(15)

    def test_chunked_by_partsize_divisible (self):
        parts1 = sequtils.chunked_by_partsize (self.seq1, partsize=5)
        expected1 = [
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14]
        ]
        self.assertListEqual (parts1, expected1)

    def test_chunked_by_partsize_nondivisible (self):
        parts1 = sequtils.chunked_by_partsize (self.seq1, 4)
        expected1 = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14]
        ]
        self.assertListEqual (parts1, expected1)

    def test_chunked_by_numparts_divisible (self):
        parts1 = sequtils.chunked_by_numparts (self.seq1, numparts=5)
        expected1 = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 10, 11],
            [12, 13, 14]
        ]
        self.assertListEqual (parts1, expected1)

    def test_chunked_by_numparts_nondivisible (self):
        parts1 = sequtils.chunked_by_numparts (self.seq1, 6)
        expected1 = [
            [0, 1, 12],
            [2, 3, 13],
            [4, 5, 14],
            [6, 7],
            [8, 9],
            [10, 11]
        ]
        self.assertListEqual (parts1, expected1)


if __name__ == '__main__':
    unittest.main()
