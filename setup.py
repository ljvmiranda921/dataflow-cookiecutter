# -*- coding: utf-8 -*-

# Import modules
from setuptools import find_packages, setup

with open("README.md", encoding="utf8") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dataflow-cookiecutter",
    version="1.0.0-alpha.1",
    author="Lester James V. Miranda",
    description="Command-line utility for creating Dataflow projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email="ljvmiranda@gmail.com",
    packages=find_packages(exclude=["docs", "tests", "templates"]),
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        "console_scripts": ["dataflow-cookiecutter=dataflow_cookiecutter.cli.main:main"]
    },
)
