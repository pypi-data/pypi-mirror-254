"""Setup for python_freeathome_local python package."""
from __future__ import annotations

from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "python_freeathome_local"
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

VERSION = {}
# pylint: disable=exec-used
with open(
    path.join(HERE, PACKAGE_NAME, "__version__.py"), encoding="utf-8"
) as fp:
    exec(fp.read(), VERSION)

PACKAGES = find_packages(exclude=["dist", "build"])

REQUIRES = ["aiohttp>=3.9.1"]

setup(
    name=PACKAGE_NAME,
    version=VERSION["__version__"],
    license="MIT License",
    url="https://github.com/derjoerg/python_freeathome_local",
    download_url="https://github.com/derjoerg/python_freeathome_local/tarball/"
    + VERSION["__version__"],
    author="Joerg Schoppet",
    author_email="joerg@schoppet.de",
    description="Python Library to communicate with local Busch-Jaeger Free@Home REST API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=PACKAGES,
    package_data={"python_freeathome_local": ["py.typed"]},
    zip_safe=False,
    platforms="any",
    python_requires=">=3.11",
    install_requires=REQUIRES,
    keywords=["freeathome", "busch-jaeger", "rest", "home", "automation"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Home Automation",
    ],
)
