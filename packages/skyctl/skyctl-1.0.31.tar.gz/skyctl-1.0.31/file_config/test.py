#!/usr/bin/env python3
import configparser

import requests
import os
import click
import tarfile


@click.group()
def login():
    """这是登录命令行接口的根命令"""
    pass


@login.command('login')
@click.option('--username', prompt=True, help='Username for login')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Password for login')
def auth(username, password):
    if username == 'admin' and password == 'password':
        click.echo('Login successful!')
    else:
        click.echo('Invalid username or password!')
        exit(1)


@login.command('check')
def check():
    click.echo('You are now in check command')
