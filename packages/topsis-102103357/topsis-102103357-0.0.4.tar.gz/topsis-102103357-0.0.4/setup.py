

import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="topsis-102103357",
    version="0.0.4",
    description="Comparison of models using Topsis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Khushi",
    author_email="",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.6',
)