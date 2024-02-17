# setup.py
from setuptools import setup, find_packages

setup(
    name="tfana",
    version="0.1.1",
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
