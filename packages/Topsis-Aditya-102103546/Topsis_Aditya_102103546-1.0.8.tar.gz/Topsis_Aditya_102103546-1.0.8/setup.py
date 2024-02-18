import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis_Aditya_102103546",
    version="1.0.8",
    description="This Python script implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) algorithm.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BROWNcoder4946/Topsis_pypi_package",
    author="Aditya Vashishta",
    author_email="adityavashishta3911@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
    packages=["Topsis"],
    include_package_data=True,
    install_requires=['pandas','numpy'],
    entry_points={
        "console_scripts": [
            "Topsis=Topsis.__main__:TOPSIS",
        ]
    },
)