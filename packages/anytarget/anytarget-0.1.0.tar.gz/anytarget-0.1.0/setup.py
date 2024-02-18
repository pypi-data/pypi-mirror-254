#!/usr/bin/env python3

import io
import sys
from setuptools import find_packages, setup
from anytarget import __author__, __version__


if sys.version_info < (3,10):
    raise ValueError("This script requires Python 3.10 or later")


setup(
    name="anytarget",
    version=__version__,
    description="This cli created to seamlessly interact with anytarget.net API",
    long_description_content_type="text/markdown",
    author=__author__,
    author_email="pyplus@protonmail.com",
    license="MIT",
    install_requires=["click>=8.1.7", "httpx>=0.26.0", "keyring>=24.3.0", "tabulate>=0.9.0", "tqdm>=4.66.1"],

    entry_points={
        "console_scripts": [
            "anytarget = anytarget:cli",
        ]
    },
    project_urls = {
        "website" : "https://anytarget.net",
        "source"  : "https://github.com/caelghoul/anytarget"
        },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    keywords="anytarget",
    python_requires=">=3.10",
    packages=find_packages(),
    include_package_data=True,

)
