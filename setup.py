import os

from setuptools import find_packages
from setuptools import setup

requires = ["peewee", "pyyaml", "flake8"]

rst_path = os.path.join(os.path.dirname(__file__), "README.md")
description = ""
with open(rst_path) as f:
    description = f.read()

setup(
    name="peewee_seed",
    version="0.1.3",
    author="Takeru Hayasaka",
    author_email="taketarou2@gmail.com",
    url="https://github.com/takehaya/peewee_seed",
    description="peewee_seed is simple data seeder using peewee.",
    long_description=description,
    license="MIT",
    platforms="any",
    packages=find_packages(exclude=("tests",)),
    package_dir={"": "."},
    install_requires=requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Database",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=requires,
    test_suite="tests",
)
