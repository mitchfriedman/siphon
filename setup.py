#name =!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='Siphon',
    version='0.0.1',
    author='mitch',
    author_email='mitchfriedman@gmail.com',
    description='Redis-backed python queue',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'clint', 'flake8',
    ],
    entry_points={
        'console_scripts': [
            'siphon = siphon.application:run',
        ]
    },
)

