# colanderpy

A simple version of the Sieve of Eratosthenes.

Developed during "Python for Scientific Computing" course at CINECA

## Install from source

Clone repository
```bash
git clone https://gitlab.hpc.cineca.it/cineca-hpyc/colanderpy.git
```

and install
```bash
$ cd pycolander
$ python setup.py install
```

## Install from Python Package Index (PyPI)

```bash
pip install pycolander
```

## Usage

### Prime number generator

```bash
$ sieve -n 42
2 3 5 7 11 13 17 19 23 29 31 37 41
```

```bash
$ sieve -h
usage: sieve [-h] [-n LIMIT]

The Sieve of Eratosthenes.

Returns the list of prime numbers up to a maximum integer.

optional arguments:
  -h, --help            show this help message and exit
  -n LIMIT, --limit LIMIT
                        maximum integer up to which the prime numbers are searched. (default 100)
```

### Prime-counting function

```bash
$ prime-counting -n 42
13
```

```bash
$ prime-counting -h
usage: prime-counting [-h] [-n LIMIT]

Prime-counting function

Counts the number of prime numbers less than or equal to an integer number.

optional arguments:
  -h, --help            show this help message and exit
  -n LIMIT, --limit LIMIT
                        maximum integer up to which the prime numbers are counted. (default 100)
```
