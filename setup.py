#!/usr/bin/env python

from distutils.core import setup

setup(
    name='pickmail',
    version='0.9',
    author='Ernest W. Durbin III',
    packages=['pickmail'],
    scripts=['bin/pickmail'],
    author_email='ewdurbin@gmail.com',
    description='pickup a single imap message',
    package_dir={'pickmail': 'pickmail'}
)
