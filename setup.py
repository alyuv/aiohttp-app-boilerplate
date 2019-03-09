import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand
from aiohttp_app_boilerplate.utils import read_build_version

HERE = os.path.realpath(os.path.dirname(__file__))


with open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(
    name='aiohttp-app-boilerplate',
    version=read_build_version(),
    description='App boilerplate for aiohttp projects',
    long_description=README,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: POSIX :: Linux",
        "Framework :: Aiohttp",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    author='Yuvchenko',
    author_email='app_boilerplate_dev@test.com',
    keywords='web asyncio aiohttp',
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    python_requires='>=3.7.1',
    dependency_links=[],
    entry_points="""\
        [console_scripts]
        aiohttp-app-boilerplate-service=aiohttp_app_boilerplate.main:main
    """,
)