# setup.py
from setuptools import setup, find_packages
from percentum import __version__

with open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="percentum",
    version=__version__,
    author="Darshan P.",
    author_email="drshnp@outlook.com",
    license='MIT',
    description="A CLI application for the percentage of the day.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/1darshanpatil/percentum',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sand=percentum.cli:start"
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.2",
    keywords="time, clock, hourglass, arena",
    project_urls={
        "Documentation": "https://github.com/1darshanpatil/percentum#readme",
        "Source": "https://github.com/1darshanpatil/percentum",
        "Tracker": "https://github.com/1darshanpatil/xpost/issues",
    },
)
