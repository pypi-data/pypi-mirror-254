from setuptools import setup, find_packages

str_version = '1.0.32'

setup(name='skyctl',
      version=str_version,
      description='联云迁移工具',
      author='XieJunWei',
      author_email='643657447@qq.com',
      license='MIT',
      packages=find_packages(),
      package_data={
          '': ['*.ini']
      },
      zip_safe=False,
      include_package_data=True,
      install_requires=['pypinyin', 'opencv-python', 'requests', 'configparser', 'Click'],
      python_requires='>=3',
      entry_points={
          'console_scripts': [
              'skyctl = ctl.terminal:ctl',
              'test = file_config.test:login',
          ],
      },
      )
