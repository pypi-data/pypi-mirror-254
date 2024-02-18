#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

REQUIREMENTS = ["transformers", "torch"]

TEST_REQUIREMENTS = ["pytest"]
QUALITY_REQUIREMENTS = ["black", "ruff"]

EXTRAS_REQUIREMENTS = {"dev": TEST_REQUIREMENTS + QUALITY_REQUIREMENTS}

setup(
    author="FairNLP",
    author_email="info@fairnlp.com",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Out-of-the-box anonymization for NLP.",
    install_requires=REQUIREMENTS,
    license="Apache Software License 2.0",
    include_package_data=True,
    keywords="incognito",
    name="incognito",
    packages=find_packages(include=["incognito", "incognito.*"]),
    test_suite="tests",
    tests_require=TEST_REQUIREMENTS,
    extras_require=EXTRAS_REQUIREMENTS,
    url="https://github.com/FairNLP/fairnlp",
    version="0.0.0",
    zip_safe=False,
)
