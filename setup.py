#-*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup (
    name = 'github_pushbullet',
    version = '0.0.2',

    author = 'taeguk',
    author_email = 'xornrbboy@gmail.com',
    
    url = 'https://github.com/taeguk/github_pushbullet',
    license='MIT',
    description = "Push github notifications to pushbullet.",
    long_description = long_description,
    
    packages=find_packages(),
    include_package_data = True,

    install_requires = ['github_listener', 'pushbullet'],
    
    keywords = 'github notification push pushbullet',
)
