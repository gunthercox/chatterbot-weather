#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Dynamically retrieve the version information from the chatterbot module
CHATTERBOT = __import__('chatterbot_weather')
VERSION = CHATTERBOT.__version__
AUTHOR = CHATTERBOT.__author__
AUTHOR_EMAIL = CHATTERBOT.__email__
URL = CHATTERBOT.__url__
DESCRIPTION = CHATTERBOT.__doc__

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as history_file:
    requirements = history_file.read()

with open('requirements_dev.txt') as dev_file:
    test_requirements = dev_file.read()

setup(
    name='chatterbot-weather',
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=[
        'chatterbot_weather',
    ],
    package_dir={'chatterbot-weather': 'chatterbot-weather'},
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.4, <4',
    license="BSD",
    zip_safe=True,
    keywords='chatterbot-weather',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
