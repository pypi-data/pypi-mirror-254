from setuptools import setup, find_packages

import json
import os

import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


def read_pipenv_dependencies(fname):
    """Get default dependencies from Pipfile.lock."""
    filepath = os.path.join(os.path.dirname(__file__), fname)
    with open(filepath) as lockfile:
        lockjson = json.load(lockfile)
        return [dependency for dependency in lockjson.get('default')]


if __name__ == "__main__":
    setup(
        name='Izok',
        version=os.getenv('PACKAGE_VERSION', get_version("./src/izok/__init__.py")),
        package_dir={'':'src'},
        packages=find_packages('src'),
        description='Izok is an open source Python-based software package that allows you to formulate an optimization problem in an easy-to-learn and efficient modeling language similar to other modeling languages AMPL, AIMMS and GAMS, and then automatically implement it in open source software package Pyomo. ',
    )