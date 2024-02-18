<!-- <div align="center"> -->
<a href="https://github.com/smartycope/Cope/actions/workflows/unit-tests.yml">
    <img src="https://github.com/smartycope/Cope/actions/workflows/unit-tests.yml/badge.svg" alt="Unit Tests">
</a>
<a href="https://pypi.org/project/Cope/">
    <img src="https://img.shields.io/pypi/v/Cope.svg" alt="PyPI Latest Release">
</a>
<!-- </div> -->

# Cope

This is my personal "standard library" of all the generally useful code I've written for various projects over the years. Pretty much any time I've written a function or class and thought "this might be useful later", I've stuffed it in here.

**Table of Contents**
* [Modules](#modules)
* [Documentation](#documentation)
* [Organization](#organization)
* [Installation](#installation)
* [License](#license)


## Modules
The currently available sub-modules are as follows:
- base
    - The main module has a bunch of misc. functions, classes, and decorators
- experimental
    - Full of all the stuff that needs rewriting, reviewing, debugging, testing, or detailing in order to be properly included. Subject to breaking API changes.
- boilerplate
    - Some things I can just never remember how to do off the top of my head. Like decorator syntax. This is just full of strings (no code) of how to do certain things.
- pygame
    - Some misc. functions relating to the pygame library
- gym
    - Includes the SimpleGym class, which adds some features to the gymnasium (formerly gym) library
- linalg
    - Not available yet, I need to go through and move them out of experimental
    - Some linear algebra functions & classes to make linear algebra easier, including a matrix() function to make inputting matricies easier


## Documentation
I don't have proper documentation yet. I need to learn a doc generator or two to learn to use those. Meanwhile, all the relevant documentation for each of the classes & functions should be in their doc strings.


## Organization
I'm trying to keep it organized and stable, so I don't have project breaking on me whenever I make changes, so I'm implementing proper semantic versioning, and the following rules:
- All classes and functions should have:
    - Doc strings
    - Tests (even if it's given to the user to see if it looks right)
    - Declared types, when possible
    - Snake_case (I've made up my mind, snake_case is standard in Python)
- Everything should be grouped together into sub-modules where possible, to keep things organized and to manage dependencies

Anything I have written that doesn't follow these rules, should be under the "experimental" sub-module, which is subject to breaking API changes.


## Installation
Cope is distributed on [PyPI](https://pypi.org) as a universal wheel and is available on Linux/macOS and Windows and supports Python 3.10+ and PyPy.

```bash
$ pip install Cope
```


## License
Cope is distributed under the [MIT License](https://choosealicense.com/licenses/mit)
