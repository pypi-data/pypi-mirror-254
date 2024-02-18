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
              default='default', required=False)
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


# 定义统一入口函数，用于调用各个命令组和子命令
def cli():
    """主函数，作为统一入口"""
    commands = [login, upload, namespace]  # 包含所有命令组的列表
    for cmd in commands:
        cmd()  # 调用每个命令组，使其注册到click中
        click.echo(f"\n---\n{cmd.__name__} commands:")  # 打印当前命令组的名称和可用的子命令列表
        for cmd_name in cmd.commands:  # 遍历当前命令组下的所有子命令，并打印它们的名称和帮助信息
            click.echo(f"{cmd_name} - {cmd.commands[cmd_name].short_help}")
        click.echo("\n---\n")  # 打印分隔线，方便区分不同的命令组和子命令列表
    # 在这里，可以根据需要进一步扩展主函数的功能，比如处理参数、调用子命令等
