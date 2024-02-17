import pathlib

import setuptools

setuptools.setup(
    name="iag_sdk",
    version="2024.1b1",
    description="Lightweight SDK to simplify the process of interacting with the Itential Automation Gateway API.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/awetomate/itential-iag-sdk",
    author="John Frauchiger",
    author_email="john@awetomate.net",
    license="MIT",
    project_urls={
        "Documentation": "https://github.com/awetomate/itential-iag-sdk",
        "Source": "https://github.com/awetomate/itential-iag-sdk",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities"
    ],
    python_requires=">=3.9,<3.12",
    install_requires=[
        "requests",
        "pydantic >=2.5.0, <3.0.0",
        ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
