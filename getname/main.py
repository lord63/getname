#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from os import path

import click

from getname import __version__
from getname.utils import UniqueRandomArray


ROOT = path.abspath(path.dirname(__file__))


@click.group(context_settings={'help_option_names': ('-h', '--help')})
@click.version_option(__version__, '-v', '--version', message='%(version)s')
def cli():
    """Get popular cat/dog/superhero/supervillain names."""
    pass


@cli.command()
@click.option('--showall', is_flag=True,
              help='Top 100 cat names in alphabetical order.')
def cat(showall):
    """Get popular cat names."""
    with open(path.join(ROOT, 'data/cat_names.json')) as f:
        cat_names = json.load(f)
    if showall:
        for name in cat_names:
            click.echo(name)
    else:
        random_name = UniqueRandomArray(cat_names).rand()
        click.echo(random_name)


@cli.command()
@click.option('-f', '--female', is_flag=True,
              help='Show random female dog names.')
@click.option('-m', '--male', is_flag=True,
              help='Show random male dog names.')
@click.option('--showall', is_flag=True,
              help='Top 200 dog names sorted by popularity.')
def dog(female, male, showall):
    """Get popular dog names."""
    if female and not showall:
        female_dog_names = load_names('female_dog')
        random_name = UniqueRandomArray(female_dog_names).rand()
        click.echo(random_name)
    if male and not showall:
        male_dog_names = load_names('male_dog')
        random_name = UniqueRandomArray(male_dog_names).rand()
        click.echo(random_name)
    if showall:
        female_dog_names = load_names('female_dog')
        male_dog_names = load_names('male_dog')
        all_dog_names = female_dog_names + male_dog_names

        if female and not male:
            names = female_dog_names
        elif male and not female:
            names = male_dog_names
        else:
            names = all_dog_names

        for name in names:
            click.echo(name)
