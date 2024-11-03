from setuptools import setup, find_packages

setup(
    name="codebreak",
    version="0.1",
    packages=find_packages(),
    description="A lighthearted package for random stretch suggestions.",
    author="Your Team",
    install_requires=[
        "pip==24.2",
        "pytest==8.3.3",
        "schedule==1.2.2",
        "setuptools==65.5.0"
    ],
    packages=find_packages(),
    python_requires=">=3.6",
     
)

