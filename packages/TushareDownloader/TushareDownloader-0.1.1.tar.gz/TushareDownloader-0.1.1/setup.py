"""
TushareDownloader setup file
"""

from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


with open("requirements.txt") as f:
    requirements: list[str] = f.read().splitlines()

setup(
    name="TushareDownloader",
    version="v0.1.1",
    author="Yanzhong Huang",
    author_email="yanzhong.huang@outlook.com",
    description="A tool to download China stock market data from Tushare.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yanzhong-Hub/TushareDownloader",
    packages=find_packages(),
    python_requires=">=3.11",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_data={
        '': ['*.txt', '*.json']
    },
    extras_require={
        "dev": [
            "pytest>=7.0",
            "twine>=4.0.2",]
    },
    install_requires=requirements
)
