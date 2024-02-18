#!/usr/bin/env python3
import os
import tarfile
import requests
import configparser

home = os.path.expanduser('~').replace('\\', '/')
# 当前脚本的绝对路径
current_path = os.path.abspath(os.path.dirname(__file__))
upload_config = configparser.ConfigParser()
upload_config.read(current_path + '/file.ini')

# skypilot配置文件
aws = home + upload_config['file_path']['aws']
lam = home + upload_config['file_path']['lambda']
azure = home + upload_config['file_path']['azure']
gcp = home + upload_config['file_path']['gcp']
ibm = home + upload_config['file_path']['ibm']
kube = home + upload_config['file_path']['kube']
oci = home + upload_config['file_path']['oci']
scp = home + upload_config['file_path']['scp']
image = 'D:/test'
# 指定要打包的目录
dirs_to_tar = [image]
# 配置文件名
config_file = upload_config['file']['file_name']


def execute(user_id, upload_url, namespace):
    if len(namespace.split()) > 2:
        print('请按正确的格式输入')
        return

    up_success_file = []
    # 创建tar文件对象
    with tarfile.open(config_file, 'w') as tar:
        # 遍历要打包的目录列表
        for dir_name in dirs_to_tar:
            # 判断文件夹是否为空
            if os.path.exists(dir_name) and os.path.isdir(dir_name):
                # 获取当前目录下的所有文件和子目录名称
                items = os.listdir(dir_name)
                # 将每个文件或子目录打包到tar文件中
                for item in items:
                    # 获取文件的完整路径
                    file_path = os.path.join(dir_name, item)
                    # 将文件添加到tar文件中
                    tar.add(file_path)
            else:
                up_success_file.append(dir_name)
    # 判断用户是否存在配置文件
    if len(up_success_file) == len(dirs_to_tar):
        print('配置文件不存在,上传失败')
        return

    if len(namespace.split()) == 1:
        data = {'userId': user_id, 'nameSpace': ''}
    else:
        data = {'userId': user_id, 'nameSpace': namespace.split()[1]}

    files = {'file': open(config_file, 'rb')}
    response = requests.post(upload_url, files=files, data=data)
    res = response.json()

    if res['code'] == 0:
        print('文件上传成功')
    elif res['code'] == 1101000003:
        print('命名空间不存在')
    else:
        print('文件上传失败')
