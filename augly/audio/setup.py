#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.

import setuptools
from pathlib import Path


VERSION = "0.1.2"
requirements = [
    r
    for r in Path("requirements.txt").read_text().splitlines()
    if '@' not in r
]


setuptools.setup(
    name="augly_audio",
    version=VERSION,
    description="A data augmentations library for audio. Submodule of augly.",
    url="https://github.com/facebookresearch/AugLy",
    author="Zoe Papakipos and Joanna Bitton",
    author_email="zoep@fb.com",
    packages=setuptools.find_packages(
        exclude=["augly.image", "augly.tests", "augly.text", "augly.video"],
    ),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
)
