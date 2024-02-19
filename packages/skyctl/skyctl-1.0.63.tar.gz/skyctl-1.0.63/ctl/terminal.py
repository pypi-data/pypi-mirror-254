#!/usr/bin/env python3
import requests
import configparser
import file_config.upload as upload
import os
import file_config.space as space


url_config = configparser.ConfigParser()
# 脚本当前的绝对路径
current_path = os.path.abspath(os.path.dirname(__file__))
url_config.read(current_path + '/server_config.ini')
login_url = url_config['server']['login_url']
upload_url = url_config['server']['upload_url']
list_url = url_config['server']['list_url']
create_url = url_config['server']['create_url']


def ctl():
    while True:
        username = input("请输入用户名(exit-退出):").strip()
        if username == 'exit':
            return
        password = input("请输入密码(exit-退出):").strip()
        if password == 'exit':
            return
        data = {'username': username, 'password': password}
        response = requests.post(login_url, data=data)
        data = response.json()

        if data['code'] == 0:
            user_id = data['data']['id']
            print("用户：" + username + "登录成功")
            while True:
                option_other = input("请输入你的选择(help —— 帮助): ").strip()
                if len(option_other.split()) > 0:
                    if option_other.split()[0] == "create":
                        space.create(create_url, user_id, option_other)
                    elif option_other.split()[0] == "upload":
                        upload.execute(user_id, upload_url, option_other)
                    elif option_other == "list":
                        space.get_list(list_url, user_id)
                    elif option_other == "help":
                        space.space_help()
                    elif option_other == "exit":
                        print("Exit Skyctl")
                        return
        else:
            print('用户名或密码错误,请重新登录')


ctl()
