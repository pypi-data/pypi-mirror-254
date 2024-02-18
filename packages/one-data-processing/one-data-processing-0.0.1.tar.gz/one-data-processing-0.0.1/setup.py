# make a setup.py for data-processing package

from typing import List

from setuptools import find_packages, setup


def load_requirements() -> List[str]:
    requirements: List[str] = []
    with open("requirements.txt", encoding="utf-8") as f:
        requirements.extend(f.readlines())
    return requirements

setup(
    name="one-data-processing",
    description="Data Processing is used for data processing through MinIO, databases, Web APIs, etc.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="PDF WORD WEB parsing preprocessing",
    url="https://github.com/kubeagi/arcadia",
    python_requires=">=3.9.0,<3.12",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    author="ggservice007",
    author_email="ggservice007@126.com",
    packages=find_packages(),
    version="0.0.1",
    install_requires=load_requirements(),
)
