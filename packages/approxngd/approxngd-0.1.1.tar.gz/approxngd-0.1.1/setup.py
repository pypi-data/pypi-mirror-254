import setuptools
from setuptools import setup, version


setuptools.setup(
    name='approxngd',
    version='0.1.1',
    author='Ragha Rao',
    author_email='ragharao2001@gmail.com',
    description='This package provides an pip installable way to implement KFAC as created by Nicholas Gao and previously by Marten et al.',
    packages=setuptools.find_packages('.'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7'
)
