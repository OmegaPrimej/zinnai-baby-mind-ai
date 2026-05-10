#!/usr/bin/env python3
"""
Setup script for Zinnai Baby Mind AI.
Install with: pip install -e .
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zinnai-baby-mind",
    version="0.2.0",
    author="OMEGA",
    description="A developmental AI that never stops learning – baby steps, giant steps, quantum CoPilot, and eternal curiosity.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourname/zinnai-baby-mind",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "pyyaml>=6.0",
        "flask>=2.0.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0", "pytest-cov"],
        "web": ["flask>=2.0.0"],
    },
    entry_points={
        "console_scripts": [
            "zinnai-console=examples.demo_console:main",
            "zinnai-dashboard=web.app:main",
        ],
    },
    include_package_data=True,
)
