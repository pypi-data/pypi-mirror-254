from setuptools import setup, find_packages

setup(
    name='UI_Framework',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pytest',
    ],
)
