from setuptools import setup, find_packages

setup(
    name="CodeShakespeare",
    version="0.1.1",
    description="A package for generating Shakespearean-style quotes and comments",
    author="Emily Huang",
    author_email="eh96@nyu.edu",
    packages=find_packages(),
    install_requires=[],  # Add dependencies if any
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
from setuptools import setup, find_packages