from setuptools import setup, find_packages

VERSION = '0.0.8'
DESCRIPTION = 'Amazon SES mail sender'
LONG_DESCRIPTION = 'Mail sender which uses the Amazon SES client'

# Setting up
setup(
    # the name must match the folder name 'amazonsessender'
    name="amazonsessender",
    version=VERSION,
    author="Adrián Carrasco Pérez",
    author_email="adrian.carrascoperez@cgi.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['boto3==1.29.1'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'boto3', which is compatible with python 3.6

    keywords=['python'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)