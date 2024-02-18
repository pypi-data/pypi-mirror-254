# !/usr/bin/env python3
import configparser
import os
from typing import Optional

import click
import requests
from cryptography.fernet import Fernet

url_config = configparser.ConfigParser()
# 脚本当前的绝对路径
current_path = os.path.abspath(os.path.dirname(__file__))
url_config.read(current_path + '/server_config.ini')
login_url = url_config['server']['login_url']
upload_url = url_config['server']['upload_url']
list_url = url_config['server']['list_url']
create_url = url_config['server']['create_url']


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
    data = {'username': username, 'password': password}
    response = requests.post(login_url, data=data)
    data = response.json()
    if data['code'] == 0:
        user_id = data['data']['id']
        encryption(username, password, user_id)
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


def encryption(account, pwd, user_id):
    # 生成密钥
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # 加密用户id
    uid = str(user_id).encode()
    encrypted_uid = cipher_suite.encrypt(uid)

    # 加密账号
    account_byte = account.encode()  # 密码需要是bytes类型
    encrypted_account = cipher_suite.encrypt(account_byte)

    # 加密密码
    password = pwd.encode()  # 密码需要是bytes类型
    encrypted_password = cipher_suite.encrypt(password)

    # 将加密后的密码和密钥保存到安全的地方
    print(f"Encrypted Uid: {encrypted_uid.decode()}")
    print(f"Key: {key.decode()}")
    print(f"Encrypted Password: {encrypted_account.decode()}")
    print(f"Key: {key.decode()}")
    print(f"Encrypted Password: {encrypted_password.decode()}")
    print(f"Key: {key.decode()}")


cli = click.CommandCollection(sources=[login, upload, namespace])

if __name__ == '__main__':
    cli()
