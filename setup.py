from setuptools import setup, find_packages

import hello_world

setup(
  name='Hello World',
  version=hello_world.__version__,
  author=hello_world.__author__,
  url='https://databricks.com',
  author_email='john.doe@databricks.com',
  description='my test wheel',
  packages=find_packages(include=['hello_world']),
  entry_points={
    'group_1': 'run=hello_world.hello:main'
  },
  install_requires=[
    'setuptools'
  ]
)
