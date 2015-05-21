#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    utils.py
    ~~~~~~~~

    some help functions.

    :copyright: (c) 2015 by lord63.
    :license: MIT, see LICENSE for more details.
"""

from __future__ import absolute_import, unicode_literals

import random
import json
from os import path

import click


ROOT = path.abspath(path.dirname(__file__))


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


def load_names(the_type):
    """Load names from the json file."""
    json_file = path.join('data', the_type + '_names.json')
    with open(path.join(ROOT, json_file)) as f:
        names = json.load(f)
    return names


def generate_random_name(the_type, showall):
    """Generate a name or print them all according to the type."""
    names = load_names(the_type)
    if showall:
        for name in names:
            click.echo(name)
    else:
        random_name = UniqueRandomArray(names).rand()
        click.echo(random_name)
