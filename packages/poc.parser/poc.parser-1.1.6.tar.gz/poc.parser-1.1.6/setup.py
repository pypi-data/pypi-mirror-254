from __future__ import print_function
from setuptools import setup, find_packages


setup(
    name='poc.parser',
    version='1.1.6',
    description="poc framework",
    author="",
    author_email="",
    packages=find_packages(),
    install_requires=[
        "PyYAML>=5.3.1",
        "charset_normalizer>=2,<4",
        "idna>=2.5,<4",
        "urllib3==1.23",
        "certifi>=2017.4.17",
        "PySocks==1.7.1"
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.7",
    scripts=["poc_parser/proxychainwrap.sh"]
)
