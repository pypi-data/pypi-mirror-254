# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))


# This call to setup() does all the work
setup(
    name="cr-nlp",
    version="0.1.0",
    description="Demo library",
    url="https://medium-multiply.readthedocs.io/",
    author="Joffrey Bienvenu",
    author_email="example@email.com",
    license="MIT",
    long_description="not much",
    long_description_content_type='text/markdown',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=[""],
    include_package_data=True,
    install_requires=["transformers"]
)