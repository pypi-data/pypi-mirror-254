#!/usr/bin/env python3
import configparser

import requests
import os
import click
import tarfile


@click.command()
@click.option('--name', default='World', help='Your name')
def hello(name):
    click.echo(f"Hello, {name}!")
