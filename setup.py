from setuptools import setup, find_packages

setup(
    name="funky_fortune",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    author="Bug Creator",
    description="divination Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/software-students-fall2024/3-python-package-bug-creator-v3",
)
