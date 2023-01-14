# Description

This repository contains an implementation of a job application task.
The task it to implement an optimization algorithm written in a script language
that interacts with an objective written in a compiled language.

The project is implemented using Python as a script language and C++
as a compiled language with the binding using Cython.

## Installation

Create `conda` environment:

    conda env create -f environment.yml

Install pre-commit hook for `git` such that code quality checks are done
automatically before every `git` commit:

    pre-commit install
