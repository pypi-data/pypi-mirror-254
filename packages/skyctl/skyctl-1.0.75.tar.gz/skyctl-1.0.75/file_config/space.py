import click
import requests


def get_list(url, user_id):
    data = {'userId': user_id}
    response = requests.post(url, data=data)
    res = response.json()
    space_list = res['data']
    str_name = ''
    for space in space_list:
        str_name += space + ' '
    click.echo(f'Namespace:\n{str_name}')


def create(url, user_id, space_name: str):
    data = {'createSource': user_id, 'nameSpace': space_name}
    response = requests.post(url, data=data)
    res = response.json()
    if res['code'] == 1101000004:
        click.echo('The namespace already exists')


def space_help():
    print('Usage:  COMMAND  [Option]')
    print('Common Commands: \n'
          'list                  Display namespace list\n'
          'create [namespace]    Create a namespace and  The [namespace] represents the name you need to create\n'
          'upload [namespace]    Upload the configuration file to the specified namespace. If the [namespace] is \n'
          '                      empty,upload it to the default namespace\n'
          'exit                  Exit Skyctl terminal')
