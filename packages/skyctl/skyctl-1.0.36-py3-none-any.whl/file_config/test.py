#!/usr/bin/env python3
import configparser

import requests
import os
import click
import tarfile


@click.group()
def login():
    """SkyCtl Login CLI."""
    pass


@login.command('login', help='Login Skyctl')
@click.option('--username', '-u', prompt=True, help='Username for login')
@click.option('--password', '-pwd', prompt=True, hide_input=True, confirmation_prompt=True, help='Password for login')
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


@upload.command('upload', help='Upload skypilot configuration file')
@click.option('--namespace', '-n', help='Namespace for file upload, if namespace is empty, upload to default',
              required=False)
def file(space):
    if space:
        click.echo("开始上传文件....")
    else:
        click.echo("开始上传文件默认....")


@click.group()
def namespace():
    """SkyCtl Namespace CLI."""
    pass


@namespace.command('namespace', help='Operation of Namespace')
@click.option('--create', '-c', help='Create a namespace')
@click.option('--list', '-l', help='Show the namespace list')
def create_space(name, ls):
    if name:
        click.echo('创建namespace = ', name)
    if ls:
        click.echo('创建namespace列表')


def cli():
    login()
    upload()
    namespace()

