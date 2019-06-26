#!/usr/bin/env python
"""render django template file"""
# -*- coding: utf-8 -*-
import click
from django.conf import settings
from django.template import Engine, Context
import json
import os
import sys

MODULE_NAME = "django_template_cli"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s path' % MODULE_NAME


@click.command()
@click.argument('path', required=True)
def _cli(path):
    settings.configure()
    context = {}
    context_path = os.path.join(os.path.dirname(path),"context.json")
    if os.path.exists(context_path):
        context = json.loads(open(context_path).read())

    tmp = Engine().from_string(open(path).read())
    out = tmp.render(Context(context))
    print(out)

if __name__=="__main__":
    _cli()

