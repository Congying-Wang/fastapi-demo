"""Python setup.py for fastapi_demo package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("fastapi_demo", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="fastapi_demo",
    version=read("fastapi_demo", "VERSION"),
    description="Awesome fastapi_demo created by Congying-Wang",
    url="https://github.com/Congying-Wang/fastapi-demo/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Congying-Wang",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["fastapi_demo = fastapi_demo.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
