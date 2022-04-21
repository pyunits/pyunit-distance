#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2022/4/21 16:05
# @Email: jtyoui@qq.com
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_text = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().strip().splitlines()

setup(
    name="pyunit_distance",
    version="1.0.0",
    description="计算距离模块集合",
    long_description=long_text,
    long_description_content_type="text/markdown",
    url='https://github.com/PyUnit/pyunit-distance',
    author="张伟",
    author_email="jtyoui@qq.com",
    license='MIT Licence',
    packages=find_packages(),
    package_data={'': ['*']},
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
