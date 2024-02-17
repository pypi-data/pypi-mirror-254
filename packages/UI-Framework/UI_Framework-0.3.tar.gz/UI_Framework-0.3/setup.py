from setuptools import setup, find_packages
setup(
    name='UI_Framework',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'pytest',
    ],
)
