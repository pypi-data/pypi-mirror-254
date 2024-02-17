from io import open
from setuptools import setup

"""
:authors: Random4ik
:license: Apache License, Vetsion 2.0, see LICENCE file
:copyring: (c) 2023 RKCompany
"""

version = '0.1.1'

'''
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
'''

long_description = '''Python module from create and check payments'''

setup(
    name='rkdonate',
    version=version,

    author='Random4ik',
    author_email='froksibrohs@gmail.com',

    description=(
        u'Python library made in Visual Studio Code using the rkdonate project https://donate.rkprojects.ru'
    ),
    long_description=long_description,

    url="https://github.com/Random4ikYT/rkdonate",
    download_url='https://github.com/Random4ikYT/rkdonate/archive/refs/heads/main.zip',
    license='Apache License, Version 2.0, see LICENSE file',

    packages=['rkdonate'],
    install_reequires=['requests', 'webbrowser'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation',
    ]
)
