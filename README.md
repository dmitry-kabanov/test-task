# Description

[![build](https://github.com/dmitry-kabanov/test-task/actions/workflows/build.yml/badge.svg)](https://github.com/dmitry-kabanov/test-task/actions/workflows/build.yml)

This repository contains an implementation of a job application task.
The task it to implement an optimization algorithm written in a script language
that interacts with an objective written in a compiled language.

The project is implemented using Python as a script language and C++
as a compiled language with the binding using Cython.

## Installation

This is a normal installation (does not work as the package is not on PyPI):

    pip install optimize

## Installation for developers

### Installation using conda

Create `conda` environment:

    conda env create -f environment.yml -n myenv
    conda activate myenv

2. Install editable version with development dependencies:

   pip install -e ".[dev]"  # quotes are needed for zsh

3. (Optional) Install pre-commit hook

Install pre-commit hook for `git` such that code quality checks are done
automatically before every `git` commit:

    pre-commit install
