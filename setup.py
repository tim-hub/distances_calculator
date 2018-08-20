import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="distances_calculator",
    keywords='distance distances_calculator, open street map, csv, big data',
    version="0.0.9",
    author="tim-hub",

    description="Calculate distances between 2 addresses, Distances Calculator is based on open street map api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim-hub/distances_calculator",
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
    ],
    entry_points = {
        'console_scripts': ['distances-calc=distances_calculator.command_line:main'],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)