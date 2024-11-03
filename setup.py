from setuptools import setup, find_packages

setup(
    name="fortunes",
    version="0.1.0",
    author="Yuhao Sheng ",
    author_email="ys4689@nyu.edu",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_project_name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "fortunes": ["fortune.txt"],  # Ensure fortune.txt is included
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "python-dotenv",  # Your runtime dependencies
    ],
    extras_require={
        "dev": ["pytest"],  # Your development dependencies
    },
)