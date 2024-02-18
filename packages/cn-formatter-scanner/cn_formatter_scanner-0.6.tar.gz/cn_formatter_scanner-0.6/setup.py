from setuptools import setup, find_packages

setup(
    name='cn_formatter_scanner',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'pytest>=7.4.4'
        'Unidecode>=1.3.8'
    ],
    author='M Usman Tahir',
    author_email='usman@cuddlynest.com',
    description='This Python package provides a title formatter for cuddlynest properties',
    long_description='This Python package provides a title formatter for cuddlynest properties as per the requirment'

)
