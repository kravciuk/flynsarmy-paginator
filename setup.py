from setuptools import setup
import sys

setup(
    # Basic package information.
    name = 'flynsarmy_paginator',
    version = '1.1.0',
    packages = ['flynsarmy_paginator'],
    include_package_data = True,
    install_requires = [],
    url = 'https://github.com/kravciuk/flynsarmy-paginator',
    keywords = 'flynsarmy paginator',
    description = 'Pagination for Django',
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

