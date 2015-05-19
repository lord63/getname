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
