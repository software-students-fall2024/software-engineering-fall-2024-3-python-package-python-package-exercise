from setuptools import setup, find_packages

setup(
    name="virtualpet",
    version="0.1.0",
    description="A virtual pet simulator package.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  
    author="Applejam-ovo",
    author_email="ql2138@nyu.edu",
    url="https://github.com/software-students-fall2024/3-python-package-straight-a",
    packages=find_packages(exclude=["tests"]),  
    python_requires=">=3.7", 
    install_requires=[],
)