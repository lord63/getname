#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import json
from os import path
from itertools import chain

import click

from getname import __version__
from getname.utils import UniqueRandomArray


ROOT = path.abspath(path.dirname(__file__))


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
    generate_random_name('cat', showall)


@cli.command()
@click.option('-f', '--female', is_flag=True,
              help='Show random female dog names.')
@click.option('-m', '--male', is_flag=True,
              help='Show random male dog names.')
@click.option('--showall', is_flag=True,
              help='Top 200 dog names sorted by popularity.')
def dog(female, male, showall):
    """Get popular dog names."""
    names = load_names('dog')
    if not showall:
        if female and not male:
            random_name = UniqueRandomArray(names['female']).rand()
        elif male and not female:
            random_name = UniqueRandomArray(names['male']).rand()
        else:
            all_dog_names = list(chain(*names.values()))
            random_name = UniqueRandomArray(all_dog_names).rand()
        click.echo(random_name)
    else:
        if female and not male:
            names = names['female']
        elif male and not female:
            names = names['male']
        else:
            names = list(chain(*names.values()))
        for name in names:
            click.echo(name)


@cli.command()
@click.option('--showall', is_flag=True,
              help='All superhero names in alphabetical order.')
def hero(showall):
    """Get superhero names."""
    generate_random_name('superhero', showall)


@cli.command()
@click.option('--showall', is_flag=True,
              help='All supervillain names in alphabetical order.')
def villain(showall):
    """Get supervillain names."""
    generate_random_name('supervillain', showall)
