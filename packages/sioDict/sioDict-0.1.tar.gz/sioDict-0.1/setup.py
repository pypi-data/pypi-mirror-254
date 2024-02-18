from setuptools import setup

setup(
    name="sioDict",
    description="A simple implementation of dict with io : runtime sync",
    version="0.1",
    packages=["sioDict", "sioDict.variants"],
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    python_requires=">=3.6",
    author="ZackaryW"
)