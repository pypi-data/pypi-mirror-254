#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
from setuptools import setup, find_packages

import ysfutils as package

if __name__ == "__main__":
    # Package name
    PKG_NAME = package.__name__

    # GitHub user name
    try:
        GITHUB_USERNAME = package.__github_username__
    except AttributeError:
        GITHUB_USERNAME = "Unknown-Github-Username"
        raise

    # Short description will be the description on PyPI
    try:
        SHORT_DESCRIPTION = package.__short_description__
    except AttributeError:
        print(
            "'__short_description__' not found in '%s.__init__.py'!" % PKG_NAME)
        SHORT_DESCRIPTION = "No short description!"
        raise

    # Long description will be the body of content on PyPI page
    try:
        LONG_DESCRIPTION = open("README.md", "rb").read().decode("utf-8")
    except FileNotFoundError:
        LONG_DESCRIPTION = "No long description!"
        raise

    # Version number, VERY IMPORTANT!
    VERSION = package.__version__

    # Author and Maintainer
    try:
        AUTHOR = package.__author__
    except AttributeError:
        AUTHOR = "Unknown"

    try:
        AUTHOR_EMAIL = package.__author_email__
    except AttributeError:
        AUTHOR_EMAIL = None

    try:
        MAINTAINER = package.__maintainer__
    except AttributeError:
        MAINTAINER = "Unknown"

    try:
        MAINTAINER_EMAIL = package.__maintainer_email__
    except AttributeError:
        MAINTAINER_EMAIL = None

    PACKAGES, INCLUDE_PACKAGE_DATA, PACKAGE_DATA, PY_MODULES = (
        None, None, None, None,
    )

    # It's a directory style package
    if os.path.exists(__file__[:-8] + PKG_NAME):
        # Include all sub packages in package directory
        PACKAGES = [PKG_NAME] + ["%s.%s" % (PKG_NAME, i)
                                 for i in find_packages(PKG_NAME)]

        # Include everything in package directory
        INCLUDE_PACKAGE_DATA = True
        PACKAGE_DATA = {
            "": ["*.*"],
        }
    # It's a single script style package
    elif os.path.exists(__file__[:-8] + PKG_NAME + ".py"):
        PY_MODULES = [PKG_NAME, ]

    # The project directory name is the GitHub repository name
    repository_name = os.path.basename(os.path.dirname(__file__))

    # Project Url
    URL = "https://github.com/{0}/{1}".format(GITHUB_USERNAME, repository_name)
    # Use today's date as GitHub release tag
    github_release_tag = 'master'
    # Source code download url
    DOWNLOAD_URL = "https://github.com/{0}/{1}/tarball/{2}".format(
        GITHUB_USERNAME, repository_name, github_release_tag)

    try:
        LICENSE = package.__license__
    except AttributeError:
        print("'__license__' not found in '%s.__init__.py'!" % PKG_NAME)
        LICENSE = ""

    PLATFORMS = [
        "MacOS",
        "Unix",
    ]

    CLASSIFIERS = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Chinese (Simplified)",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3 :: Only"
    ]

    # Read requirements.txt, ignore comments
    try:
        REQUIRES = list()
        f = open("requirements.txt", "rb")
        for line in f.read().decode("utf-8").split("\n"):
            line = line.strip()
            if "#" in line:
                line = line[:line.find("#")].strip()
            if line:
                REQUIRES.append(line)
    except FileNotFoundError:
        print("'requirements.txt' not found!")
        REQUIRES = list()

    setup(
        name=PKG_NAME,
        description=SHORT_DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        packages=PACKAGES,
        include_package_data=INCLUDE_PACKAGE_DATA,
        package_data=PACKAGE_DATA,
        py_modules=PY_MODULES,
        url=URL,
        download_url=DOWNLOAD_URL,
        classifiers=CLASSIFIERS,
        platforms=PLATFORMS,
        license=LICENSE,
        install_requires=REQUIRES,
    )
