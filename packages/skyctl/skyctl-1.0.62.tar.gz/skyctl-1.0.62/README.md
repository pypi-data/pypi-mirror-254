# 1 skyctl安装

### 1.1 skyctl的安装方式

1) 使用 pip install skyctl 安装skyctl 工具(指定安装路径 pip install requests --target=/path/to/myproject)

2) 使用 python -m site 查询skyctl 的安装路径

   (例如：/home/zdcloud/miniconda3/envs/UCTool/lib/python3.7/site-packages)

3) 将skyctl 的安装路径加入环境变量，你需要在`~/.bashrc`或`~/.bash_profile`文件中添加相应的`export`命令。这样，每次登录时都会自动设置环境变量。你可以使用文本编辑器打开这些文件，并将上述`export`命令添加到文件的末尾，然后保存并关闭文件

   （例如：export PATH=/home/zdcloud/miniconda3/envs/UCTool/lib/python3.7/site-packages/yours_package:$PATH）。最后，重新启动终端或执行以下命令使更改生效：source ~/.bashrc 或 source ~/.bash_profile

### 1.2 skyctl的更新方式

使用指令：pip install --upgrade skyctl 

# 2 skyctl使用

### 2.1 脚本运行

进入到脚本安装目录(/home/zdcloud/miniconda3/envs/UCTool/lib/python3.7/site-packages/yours_package),给terminal.py赋予执行权限 chmod +x terminal.py

运行：terminal.py

### 2.2 用户登录

使用UC会员系统账号密码进行登录

### 2.3 命令行操作

#### 2.3.1 upload

上传skypilot配置文件，所需参数：

（1）直接回车，将文件上传到default namespace

（2）输入namespace，将文件上传到指定的namespace

#### 2.3.2 create

创建namespace，所需参数：自定义namespace名称

#### 2.3.3 list

展示用户所有namespace列表

#### 2.3.4 exit

退出脚本
