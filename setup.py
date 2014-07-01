#!/usr/bin/env python

from setuptools import setup

setup(
    name='decanter',
    version='0.1.0',
    description='A front end package manager for python web apps',
    author='Zach McGrenere',
    author_email='zach@mcgrenere.com',
    url='http://decntr.com/',
    license='MIT',
    zip_safe=False,
    entry_points = {'console_scripts': ['decanter = decanter:main']},
    packages=['decanter'],
    data_files=[('config', ['config'])],
    install_requires=['argparse==1.2.1','PyYAML==3.11']
)