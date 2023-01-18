# Description

[![Test with conda](https://github.com/dmitry-kabanov/test-task/actions/workflows/test-conda.yml/badge.svg)](https://github.com/dmitry-kabanov/test-task/actions/workflows/test-conda.yml)
[![Test with pip](https://github.com/dmitry-kabanov/test-task/actions/workflows/test-pip.yml/badge.svg)](https://github.com/dmitry-kabanov/test-task/actions/workflows/test-pip.yml)

This repository contains an implementation of a job application task.
The task it to implement an optimization algorithm written in a script language
that interacts with an objective written in a compiled language.

The project is implemented using Python as a script language and C++
as a compiled language with the binding using Cython.

## Installation

## Installation for end users

This is a normal installation (does not work as the package is not on PyPI):

    pip install optimize

## Installation for developers

### Installation using conda

#. Create `conda` environment:

    conda env create -f environment.yml -n myenv
    conda activate myenv

#. Install editable version with development dependencies:

    pip install -e ".[dev]"  # quotes are needed for zsh

#. To check that installed development version works, run tests:

    pytest

### Installation using venv and pip

#. Create virtual environment:

    python -m venv venv
    source venv/bin/activate

#. Installed editable version with development dependencies:

    pip install -e ".[dev]"  # quotes are needed for zsh

#. To check that installed development version works, run tests:

    pytest

### (Optional) Install pre-commit hook

Install pre-commit hook for `git` such that code quality checks are done
automatically before every `git` commit:

    pre-commit install

## How to use the library

Example usage of the library can be found in script `bin/example.py`:

    python bin/example.py

The main details of the API are the following.
Let minimize a function that accepts an N-dimensional vector and minimizes
the sum of squares of the components of that vector.
Such a function, named `parabola_nd` is included in the library
and can be imported with

    from optimize.functionals import parabola_nd

#. Create an optimizer (for example, steepest descent optimizer),
passing parameters that control its operations:

    from optimize import SteepestDescent
    opt = SteepestDescent()

Here, we used default values of the optimizer.

#. Create an initial guess for optimization:

    x0 = [1.0, 2.0, 3.0]

#. To minimize the functional `parabola_nd` pass it to the optimizer along
with the initial guess:

    xmin = opt.minimize(parabola_nd, x0)

#. To check the reason for termination of the iterative minimization process,
use property `opt.reason` of the optimizer.
