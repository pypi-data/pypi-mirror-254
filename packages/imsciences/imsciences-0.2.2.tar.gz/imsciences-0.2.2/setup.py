from setuptools import setup, find_packages

VERSION = '0.2.2'
DESCRIPTION = 'IMS Data Processing Package'
LONG_DESCRIPTION = 'This package contains a series of functions aimed to improve the data processing process'

# Setting up
setup(
    name="imsciences",
    version=VERSION,
    author="Cameron",
    author_email='thecjrobs@gmail.com',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "pandas"
    ],
    keywords=['python', 'data processing'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
