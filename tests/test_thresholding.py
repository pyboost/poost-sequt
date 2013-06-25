#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Pengkui Luo <pengkui.luo@gmail.com>
# Created 06/25/2013, updated 06/25/2013
#
""" Unit tests for thresholding.py
"""
print('Executing %s' %  __file__)

import unittest
import os, sys, time

import poost.sequtils as sequtils


class Test_natural_cutoff (unittest.TestCase):

    def test_natural_cutoff (self):
        lo, hi = 0.2, 0.5
        self.assertAlmostEqual(
            sequtils.natural_cutoff(
                [0.28, 0.40, 0.50, 0.65],
                lo, hi
            ),
            0.28
        )
        self.assertAlmostEqual(
            sequtils.natural_cutoff(
                [0.1, 0.17, 0.21, 0.30, 0.51],
                lo, hi
            ),
            0.21
        )
        self.assertAlmostEqual(
            sequtils.natural_cutoff(
                [0.1, 0.17, 0.21, 0.28, 0.37, 0.45, 0.51],
                lo, hi
            ),
            0.2
        )


if __name__ == '__main__':
    unittest.main()
