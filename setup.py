import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distances calculator",
    version="0.0.1",
    author="tim-hub",
    author_email="github.com/tim-hub",
    description="Distances claculator based on open street map api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim-hubt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)