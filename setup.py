#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="kushum",
    author_email='kushumshow@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="demo for cookicutter",
    entry_points={
        'console_scripts': [
            'shell_cookiecutter=shell_cookiecutter.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='shell_cookiecutter',
    name='shell_cookiecutter',
    packages=find_packages(include=['shell_cookiecutter', 'shell_cookiecutter.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kushum28/shell_cookiecutter',
    version='0.1.0',
    zip_safe=False,
)
