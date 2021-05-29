#!/usr/bin/env python3
"""ALPHA VIDEO setup script."""
from datetime import datetime as dt

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

PROJECT_NAME = "Alpha Video"
PROJECT_PACKAGE_NAME = "thealphavideo"
PROJECT_LICENSE = "Apache License 2.0"
PROJECT_AUTHOR = "Unofficial-skills"
PROJECT_COPYRIGHT = f" 2021-{dt.now().year}, {PROJECT_AUTHOR}"
PROJECT_URL = "https://alpha-video.andrewstech.me/"
PROJECT_EMAIL = "hello@andrewstech.me"

PROJECT_GITHUB_USERNAME = "unofficial-skills"
PROJECT_GITHUB_REPOSITORY = "alpha-video"

PYPI_URL = f"https://pypi.python.org/pypi/{PROJECT_PACKAGE_NAME}"
GITHUB_PATH = f"{PROJECT_GITHUB_USERNAME}/{PROJECT_GITHUB_REPOSITORY}"
GITHUB_URL = f"https://github.com/{GITHUB_PATH}"

PROJECT_URLS = {
    "Bug Reports": f"{GITHUB_URL}/issues",
    "Dev Docs": "https://alpha-video.andrewstech.me/",
    "Discord": "https://discord.gg/WAu8ApjwG2",
}

PACKAGES = find_packages(exclude=["tests", "tests.*"])




setup(
    name=PROJECT_PACKAGE_NAME,
    version="1.47",
    url=PROJECT_URL,
    project_urls=PROJECT_URLS,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    package_data={'thealphavideo': ['templates/*.html']},
    zip_safe=False,
    install_requires=requirements,
    test_suite="tests",
    entry_points={"console_scripts": ["alpha-video = thealphavideo.__main__:start"]},
)
