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
    url="https://github.com/tim-hub/calculator",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'argparse',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Data Mapping :: Open Street Map',
    ],
    entry_points = {
        'console_scripts': ['distance_calculator=calculator.command_line:main'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)