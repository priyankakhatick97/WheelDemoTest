from setuptools import setup, find_packages

import hello_world
import subprocess

def get_git_version():
    try:
        # Get the latest Git tag
        version = subprocess.check_output(["git", "describe", "--tags"], stderr=subprocess.STDOUT).strip().decode('utf-8')
        return version
    except subprocess.CalledProcessError:
        return "0.0.1"  # Fallback version if no tags are found
      
setup(
  name='Myhelloworld',
  version=get_git_version(),
  author=hello_world.__author__,
  url='https://databricks.com',
  author_email='john.doe@databricks.com',
  description='my test wheel',
  packages=find_packages(include=['hello_world']),
  entry_points={
    'group_1': 'run=hello_world.__main__:main'
  },
  install_requires=[
    'setuptools'
  ]
)
