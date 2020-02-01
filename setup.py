from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

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
    package_data={
        "app": []
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "app=app.__main__"
        ],
    },
)