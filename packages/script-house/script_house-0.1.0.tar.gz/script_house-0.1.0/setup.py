from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="script_house",
    version="0.1.0",
    description="a python script house containing handy functions for daily use",
    packages=find_packages(),
    url="https://github.com/el-nino2020/script-house",
    author="El nino",
    author_email="el-nino202020@protonmail.com",
    python_requires=">=3.11",
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
