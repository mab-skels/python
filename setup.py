from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

# Collect the contents of 'requirements.txt' as a list for use in the setup definition
with open(path.join(here, "requirements.txt"), encoding="utf-8") as requirements:
    requirements_contents = requirements.read()
    requirements_list = [
        line
        for line in requirements_contents.split("\n")
        if len(line) > 0 and not line.startswith("#")
    ]

setup(
    name="app",
    version="0.0.1",
    description=long_description,
    url="",
    author="",
    author_email="",
    classifiers=[],
    keywords="",
    packages=find_packages(exclude=["tests"]),
    package_data={"app": []},
    install_requires=requirements_list,
    entry_points={"console_scripts": [f"app=app.__main__"],},
)
