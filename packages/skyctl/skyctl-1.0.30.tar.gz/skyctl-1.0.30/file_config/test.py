#!/usr/bin/env python3
import configparser

import requests
import os
import click
import tarfile


@click.group()
@click.option('--username', prompt=True, help='Username for login')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Password for login')
def login(username, password):
    if username == 'admin' and password == 'password':
        click.echo('Login successful!')
    else:
        click.echo('Invalid username or password!')
        exit(1)


@login.command(help='Check config')
def check(username, password):
    click.echo('You are now in check command')
    click.echo('Your username is {} and password is {}'.format(username, password))
