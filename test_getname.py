#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from unittest import TestCase

from itertools import chain

from getname.main import random_name, load_names


class TestGetName(TestCase):
    def test_get_cat_name(self):
        cat_names = load_names('cat')
        assert random_name('cat') in cat_names
        assert len(random_name('cat', showall=True).split('\n')) == 100
        self.assertRaises(ValueError, random_name, 'cat', 'female', True)

    def test_get_dog_name(self):
        dog_names = load_names('dog')
        assert random_name('dog') in list(chain(*dog_names.values()))
        assert random_name('dog', 'female') in dog_names['female']
        assert random_name('dog', 'male') in dog_names['male']
        assert len(random_name('dog', 'female', True).split('\n')) == 100
        assert len(random_name('dog', 'male', True).split('\n')) == 100
        assert len(random_name('dog', showall=True).split('\n')) == 200

    def test_get_superhero_name(self):
        superhero_names = load_names('superhero')
        assert random_name('superhero') in superhero_names
        assert len(random_name('superhero', showall=True).split('\n')) == 1825
        self.assertRaises(ValueError, random_name, 'superhero', 'female', True)

    def test_get_supervallain_name(self):
        supervillain_names = load_names('supervillain')
        assert random_name('supervillain') in supervillain_names
        assert len(
            random_name('supervillain', showall=True).split('\n')) == 712
        self.assertRaises(ValueError, random_name,
                          'supervillain', 'female', True)

    def test_invalid_type(self):
        self.assertRaises(ValueError, random_name, 'invalid_type')
