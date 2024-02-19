from setuptools import setup

setup(
    name="sioDict",
    description="A simple implementation of dict with io : runtime sync",
    version="0.2.0",
    packages=["sioDict", "sioDict.variants"],
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "orjson",
        "toml"
    ],
    python_requires=">=3.6",
    author="ZackaryW"
)