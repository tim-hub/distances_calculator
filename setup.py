import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distances_calculator",
    keywords='distance calculator, open street map, csv, big data',
    version="0.0.2",
    author="tim-hub",
    author_email="github.com/tim-hub",
    description="Distances claculator based on open street map api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim-hub/distance_calculator",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'time',
        'math',
        'json',
        'random',
        'pandas'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Data Mapping :: Open Street Map',
    ],
)