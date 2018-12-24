# coding: utf-8
"""
A simple module to fetch Cavelink values by parsing the HTML page of sensors.
"""

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='cavelink',
    version='1.1.1',
    author='Sébastien Pittet',
    author_email='sebastien@pittet.org',
    description='Fetch Cavelink data by parsing the webpage of sensors.',
    long_description=long_description,
    url='https://github.com/SebastienPittet/cavelink',
    keywords='speleo cave sensor',
    packages=find_packages(),
    license='MIT',
    platforms='any',
    install_requires=['python-dateutil', 'requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience'
    ]
)
