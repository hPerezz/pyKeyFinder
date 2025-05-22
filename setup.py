from setuptools import setup, find_packages

setup(
    name="pyKeyFinder",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'librosa',
        'numpy',
    ],
) 