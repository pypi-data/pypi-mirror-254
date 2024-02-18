from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.7'
DESCRIPTION = 'A Roblox API Wrapper for roblox.com'
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="RoInfo",
    version=VERSION,
    author="Ryan_shamu",
    author_email="Ryanshamu418@Gmail.com",
    description=DESCRIPTION,
    url = 'https://github.com/Ryan-shamu-YT/RoInfo',
    project_urls = {
  'Homepage': 'https://github.com/Ryan-shamu-YT/RoInfo/',
  },
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=["requests"],
    keywords=['Roblox', 'RoInfo', 'Roblox Web Api', 'Roblox Python', 'Roblox For Python', 'Roblox Api', 'Roblox Api Library', 'Roblox Bot'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)