from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r") as f:
  long_description = f.read()

setup(name='fstree',    # 包名
      version='0.0.1',        # 版本号
      description='A fscore tree for rule extraction',
      long_description=long_description,
      author='pcx',
      author_email='pengchengxia@163.com',
      url='',
      install_requires=['pandas','numpy'],	# 依赖包会同时被安装
      license='MIT',
      packages=find_packages())
