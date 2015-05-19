#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import random


class UniqueRandomArray(object):
    """Get consecutively unique elements from an array."""
    def __init__(self, sequence):
        self.previous = None
        self.sequence = sequence

    def rand(self):
        item = random.choice(self.sequence)
        if item == self.previous:
            item = self.rand()
        self.previous = item
        return item
