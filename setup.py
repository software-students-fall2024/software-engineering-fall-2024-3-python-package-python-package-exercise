# setup.py
from setuptools import setup, find_packages

setup(
<<<<<<< HEAD
    name="fortunes",
    version="0.1.0",
    author="Yuhao Sheng ",
    author_email="ys4689@nyu.edu",
    description="A fortune package",
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
    python_requires=">=3.7",
=======
    name='fortune_package',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
>>>>>>> 8c6c3d31ad7c841b9a1c0555cfae4c62e93df3a0
    install_requires=[
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'fortune=fortune_package.fortune:main',
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='A fun package that provides fortunes and quotes',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/fortune_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
