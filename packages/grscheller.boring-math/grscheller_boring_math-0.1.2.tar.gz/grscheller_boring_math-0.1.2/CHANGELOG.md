# CHANGELOG

Changelog for the grscheller.boring-math PyPI project.
Version numbers for PyPI releases begin with a `v`.

Semantic Versioning will be used:

* Semantic versioning for PyPI releases:
  * first digit means
    * A major event, epoch, or paradigm shift
  * second digit means
    * PyPI breaking API changes or PyPI major changes
  * third digit either means
    * PyPI API additions, PyPI bugfixes or minor changes
    * Significant documentation updates

## Veresion v0.1.2 - PyPI release date 2024-01-30

* now needs CircularArray v0.1.2
  * integer_math comb uses new foldL method of CircularArray
  * CircularArray was split out of grscheller.satastructures
* test suite written

## Veresion v0.1.1 - PyPI release date 2024-01-20

* fixed some negative value edge cases
  * lcm(0,0) now gives 0 instead of a divide by zero exception
    * some authors leave lcm(0, 0) as undefined
    * lcm(0, 0) = 0 does make sense
      * since a*0 = 0 for all a >= 0
      * 0 is the smallest non-negative interger a such that a*0 = 0
      * most math theorems remain true for this case
* README.md improvements

## Version v0.1.0 - PyPI release date 2024-01-17

* initial PyPI grscheller.boring-math release
* updated pyproject.toml to be in alignment with grscheller.datastrucutes

## Version 0.0.8 - commit date 2024-01-14

* changed project's name from boring_math to boring-math
* both GitHub repo and future PyPI repo
* more in alignment with what I see on PyPI
* project is grscheller.boring-math
* package is still grscheller.boring_math

## Version 0.0.8 - commit date 2024-01-14

* working on pyproject.toml infrastructure for PyPI releases
* will use Flit as the packaging/publishing tool
* replaced bin/ scripts with boring_math.integer_math_cli entry pts

## Version 0.0.4 - commit date 2024-01-10

* first coding changes in years!
* configured gh-pages

## Version 0.0.0.3 - commit date 2023-12-06

* added pyproject.toml

## Version 0.0.0.2 - commit date 2023-12-06

* got package working again
  * did not understand iterators that well when I first wrote this package
* replaced my `take` with `itertools.islice`
* generated docs from docstrings with pdoc3

## Version 0.0.0.1 - commit date 2023-12-06

* fixed Markdown issues with first commit
* Added .gitignore file to anticipate pytest & __pycache__ directories
 
## Version 0.0.0.0 - commit date 2023-12-06

* first commit of source code with with the old pipfile build
  infrastructure removed.
