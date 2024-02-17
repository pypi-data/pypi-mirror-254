# setup.py
from setuptools import setup, find_packages

import sys

version = "0.0.3"
sys.path.insert(0, ".")
setup(
    name="tfana",
    version=version,
    author_email="1691315371@qq.com",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        "console_scripts": [
            "list_rc = tfana.bin.list_rc:main",
        ],
    },
)
