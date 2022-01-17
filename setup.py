from pathlib import Path
from setuptools import setup, find_packages

with open(
    str(Path(__file__).resolve().parents[0] / "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name="nostr",
    author="Yuval Adam",
    author_email="_@yuv.al",
    version="0.1.0",
    description="Python implementation for the nostr protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuvadm/nostrpy",
    license="MIT",
    python_requires=">=3.7.0",
    packages=find_packages(exclude=["docs", "tests"]),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    entry_points={
        "console_scripts": [
            "nostr = nostr.cli:entry",
        ]
    },
)
