#! /usr/bin/env python

from setuptools import setup

setup(
    name='markdown-superscript',
    version='0.1.1',
    author='Shane Graber',
    description='Python-Markdown extension which adds superscript',
    url='https://github.com/blackrobot/markdown.superscript',
    py_modules=['mdx_superscript'],
    install_requires=['markdown>=2.0'],
    zip_safe = True,
    keywords='markdown superscript'
)
