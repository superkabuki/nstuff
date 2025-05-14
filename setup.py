#!/usr/bin/env python3

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

from nstuff import version

setuptools.setup(
    name="nstuff",
    version=version,
    author="Adrian of Doom",
    author_email="spam@iodisco.com",
    description="nstuff is a replacement for cgi.MiniFieldStorage, nstuff parses CGI POST and GET data into a dict.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/superkabuki/nstuff",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: Sleepycat License",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.8",
)
