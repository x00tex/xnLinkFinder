#!/usr/bin/env python
import os
import shutil
from setuptools import setup, find_packages

# Define the target directory for the config.yml file
target_directory = os.path.join(os.path.expanduser("~"), ".config", "xnLinkFinder") if os.path.expanduser("~") == os.path.expanduser("~" + os.environ['USER']) else None

# Copy the config.yml file to the target directory if it exists
if target_directory and os.path.isfile("config.yml"):
    os.makedirs(target_directory, exist_ok=True)
    shutil.copy("config.yml", target_directory)

setup(
    name="xnLinkFinder",
    packages=find_packages(),
    version=__import__('xnLinkFinder').__version__,
    description="A python script to find endpoints from a URL, a file of URLs, a directory of files, a Burp XML file or a ZAP ASCII message file. It also gets potential parameters and a target specific wordlist.",
    long_description=open("README.md").read(),
    author="@xnl-h4ck3r",
    url="https://github.com/xnl-h4ck3r/xnlLinkFinder",
    zip_safe=False,
    py_modules=["xnLinkFinder"],
    install_requires=["argparse","requests","psutil","pyyaml","termcolor","urlparse3","beautifulsoup4","lxml","html5lib"],
    entry_points={
        'console_scripts': [
            'xnlinkfinder = xnLinkFinder.xnLinkFinder:main',
        ],
    },
)
