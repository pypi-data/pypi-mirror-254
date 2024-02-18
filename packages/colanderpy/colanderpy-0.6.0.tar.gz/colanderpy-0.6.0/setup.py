from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()


setup(
    name="colanderpy",
    version="0.6.0",
    author="Sergio",
    author_email="s.orlandini@cineca.it",
    description="A simple version of the Sieve of Eratosthenes. Developed during \"Python for Scientific Computing\" course at CINECA",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.hpc.cineca.it/cineca-hpyc/colanderpy",
    packages=find_packages(),
    install_requires=["numpy"],
    entry_points={
        "console_scripts": [
            "sieve=colanderpy.sieve:main",
            "prime-counting=colanderpy.pi_function:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "License :: Free For Educational Use",
        "Operating System :: OS Independent",
        "Topic :: Education",
    ],
)
