#!/usr/bin/env python3
import configparser
from typing import Optional

import requests
import os
import click
import tarfile


@click.group()
def login():
    """SkyCtl Login CLI."""
    pass


@login.command('login', help='Login Skyctl')
@click.option('--username',
              '-u',
              prompt=True,
              help='Username for login')
@click.option('--password',
              '-pwd',
              prompt=True,
              hide_input=True,
              confirmation_prompt=True, help='Password for login')
def auth(username, password):
    if username == 'admin' and password == 'password':
        click.echo('Login successful!')
    else:
        click.echo('Invalid username or password!')
        exit(1)


@login.command('check', help='Check if the skyctl configuration file exists')
def check():
    click.echo('You are now in check command')


@click.group()
def upload():
    """SkyCtl Upload CLI."""
    pass


@upload.command('upload',
                help='Upload skypilot configuration file')
@click.option('--space',
              '-n',
              help='Namespace for file upload, if namespace is empty, upload to default',
              default='default',
              show_default=True,
              type=str)
def file(space: Optional[str]):
    if space:
        click.echo("开始上传文件....")
        print('上传文件到 = ', space)


@click.group()
def namespace():
    """SkyCtl Namespace CLI."""
    pass


@namespace.command('namespace', help='Operation of Namespace')
@click.option('--create',
              '-c',
              help='Create a namespace',
              type=str)
@click.option('--ls',
              '-l',
              is_flag=True,
              default=False,
              required=False,
              help='Show the namespace list')
def create_space(create: Optional[str], ls: bool):
    if create:
        click.echo('创建namespace = ')
        ls = False

    if ls:
        click.echo('namespace列表')


cli = click.CommandCollection(sources=[login, upload, namespace])

if __name__ == '__main__':
    cli()
