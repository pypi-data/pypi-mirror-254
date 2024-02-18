#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import zkyutils

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="zkyutils",
    version=zkyutils.__version__,
    author="zky",
    author_email="2221831747@qq.com",
    description="自用python工具类",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/dz-mondler/zkyutils",
    py_modules=['zkyutils'],
    install_requires=[
        "loguru <= 0.7.2",
        "pandas <= 1.1.5",
        "xlrd <= 2.0.1",
        "xlwt <= 1.3.0",
        "openpyxl <= 3.0.9",
        ],
    classifiers=[
        "Topic :: Games/Entertainment ",
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Board Games',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)

