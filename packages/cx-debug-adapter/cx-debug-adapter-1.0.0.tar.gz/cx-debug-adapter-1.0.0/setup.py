# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "cx-debug-adapter"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "setuptools>=21",
    "click",
    "esp-debug-backend",
    "requests>=2.21.0",
]
setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    description='C & CPP debugger adapter for Python',
    license="Apache License 2.0",
    platforms='any',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/volcengine/volcengine-python-sdk',
)
