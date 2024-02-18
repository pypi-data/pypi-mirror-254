###
# python setup.py sdist
# python setup.py sdist bdist_wheel
# easy_install xxx.tar.gz
# pip install -U example_package.whl
# ##

import PIL
from setuptools import setup, find_packages

setup(
    name='jinsh',# 自定义工具包的名字
    version='0.21',# 版本号
    author="Walter",  # 作者名字
    author_email="jinshuhaicc@gmail.com",  # 作者邮箱
    description="tool",  # 自定义工具包的简介
    license='MIT-0',  # 许可协议
    packages=find_packages(),
    install_requires=[
        "pillow==10.2.0",
        "oracledb==2.0.1",
        "json5==0.9.14",
        "oci==2.119.1"
    ],
)


