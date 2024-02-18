from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Amazon SES mail sender'
LONG_DESCRIPTION = 'Mail sender which uses the Amazon SES client'

# Setting up
setup(
    # the name must match the folder name 'amazon-mail-sender'
    name="amazon-mail-sender",
    version=VERSION,
    author="Adrián Carrasco Pérez",
    author_email="adrian.carrascoperez@cgi.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['boto==1.34.31'],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'amazon'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)