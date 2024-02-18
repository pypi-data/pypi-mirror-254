from setuptools import setup, find_packages

setup(
    name="cleric",
    version="0.0.1",
    author="Willem Pienaar",
    author_email="pypi@cleric.io",
    description="A simple spell casting package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/clerichq/cleric-pypi",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)

