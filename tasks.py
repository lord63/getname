#!/usr/bin/env python
# -*- coding: utf-8 -*-

from invoke import task, run


@task
def test():
    run("py.test -v test_getname.py")
    run("py.test --pep8 test_getname.py getname/*.py")
