#!/usr/bin/env python
# coding: utf-8

import setuptools
from setuptools import setup
with open("README1.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()
setup(
    name='robotgpt',
    version='0.0.14',
    author='blaze.zhang',
    author_email='blaze.zhang@cloudminds.com',
    description=u'RobotGPT LLM 支持Langchain',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['robotgpt'],
    install_requires=['langchain'],
)