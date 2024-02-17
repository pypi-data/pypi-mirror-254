from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="OhlcvAnalyser",
    version="1.0.2",
    packages=find_packages(),
    author="jackmappotion",
    author_email="jackmappotion@gmail.com",
    url="https://github.com/jackmappotion/OhlcvAnalyser",
    description="OhlcvAnalyser",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
