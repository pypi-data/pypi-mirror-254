import requests


def get_list(url, user_id):
    data = {'userId': user_id}
    response = requests.post(url, data=data)
    res = response.json()
    space_list = res['data']
    str_name = ''
    for space in space_list:
        str_name += space + ' '
    print(str_name)


def create(url, user_id, space_name: str):
    print(len(space_name.split()))
    if not len(space_name.split()) == 2:
        print('请按正确的格式输入')
        return
    space = space_name.split()[1]
    data = {'createSource': user_id, 'nameSpace': space}
    response = requests.post(url, data=data)
    res = response.json()
    if res['code'] == 1101000004:
        print('namespace已存在')


def space_help():
    print('Usage:  COMMAND  [Option]')
    print('Common Commands: \n'
          'list                  Display namespace list\n'
          'create [namespace]    Create a namespace and  The [namespace] represents the name you need to create\n'
          'upload [namespace]    Upload the configuration file to the specified namespace. If the [namespace] is \n'
          '                      empty,upload it to the default namespace\n'
          'exit                  Exit Skyctl terminal')
