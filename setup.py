#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as history_file:
    requirements = history_file.read()

with open('requirements_dev.txt') as history_file:
    test_requirements = history_file.read()

setup(
    name='chatterbot-weather',
    version='0.1.0',
    description="A ChatterBot logic adapter that returns information about the weather.",
    long_description=readme + '\n\n' + history,
    author="Gunther Cox",
    author_email='gunthercx@gmail.com',
    url='https://github.com/gunthercox/chatterbot-weather',
    packages=[
        'chatterbot_weather',
    ],
    package_dir={'chatterbot-weather':
                 'chatterbot-weather'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=True,
    keywords='chatterbot-weather',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
