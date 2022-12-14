import setuptools

from pathlib import Path

PACKAGE_NAME = "cdep_base"
DESCRIPTION = "Base package for the installation of the rest of icdep's dependencies"
URL = "https://github.com/jmartinpe/cdep_base"
AUTHOR = "John Doe"
AUTHOR_EMAIL = "jmartinpe@sia.es"
LICENSE = "UNLICENSED"
REQUIREMENTS = []

setuptools.setup(
    name=PACKAGE_NAME,
    version="0.0.1",
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    extras_require={
        "package_a": ["cdep_package_a"],
        "package_b": ["cdep_package_b"],
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    classifiers=["Programming Language :: Python :: 3"],
)
