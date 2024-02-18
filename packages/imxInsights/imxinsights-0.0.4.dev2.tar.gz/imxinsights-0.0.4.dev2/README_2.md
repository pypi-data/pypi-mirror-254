--8<-- [start:main]
 
# imxInsights
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/imxInsights)
[![PyPI version](https://badge.fury.io/py/imxInsights.svg)](https://pypi.org/project/imxInsights)
[![PyPI - Status](https://img.shields.io/pypi/status/imxInsights)](https://pypi.org/project/imxInsights/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/imxInsights)](https://pypi.org/project/imxInsights)

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](http://ansicolortags.readthedocs.io/?badge=latest)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![PyPI - License](https://img.shields.io/pypi/l/imxInsights)

Documentation: https://xxxxxx

Source Code: https://xxxxxx

!!! danger "Warning!"
    The goal for `imxInsights` is to get information from imx files, ***adding, deleting or mutating data is out of scope!***

!!! abstract
    The module will parse a imx file that can contain a Situation or a Project with a InitialSituation and a optional NewSituation. Every situation has
    a repository that contains value objects. A value object is a object of intrest and contains properties and methodes to get information. 

!!! info "Audience"
    The aimed audience are end users that just know some python, therefor imxInsights should have a minimal api that is well documented. 
    We use the awesome makedocs (plugins) to generate a neat website from documentations and markdowns.

## Features
- Value objects repository for every object of intrest, puic attribute is the key if no puic attribute use a configurable custom key.
- RailConnection geometry, constructed from junctions reffed in the microLink From- and ToNode attributes.
- TrackFragments and demarcation marker objects have projected geometry.
- Reffed objects links, access referenced objects as value objects
- Area classifier, we try to classifier every value object to a imx project area.
- Value object as dataframe, easy way to get a Pandas dataframe from value objects.
- Difference generator including excel and geojson export.

## Supported Python Versions
This library is only compatible with ***Python 3.10*** and above. 

!!! warning
    ***3.9 and below will NOT be supported***.

## Quick Start

### Distribution and installation
imxInsights is not (yet*) distributed on https://pypi.org so first we need to download and install the python wheel. This can be done by the following pip command:

``pip install x:\path\to\wheel\imxInsights-x.x.x.x-py3-none-any.whl``

***import, load file, get repo have fun!***

## Code samples and snippets
```
from imxInsight import Imx

imx = Imx(file_path)

init_repo = imx.project.initial_situation
object_of_intrest = init_repo.get_by_puic(puic)

pandas_df = imx.project.new_situation.get_pandas_df("Signal")
```

For more code samples and snippets in the example section / folder and use the api reference for exploration.

## Roadmap
- [X] imx diff
- [X] pypi release 0.0.1
- [X] documentation and webpage
- [ ] 100% code coverage 
- [ ] refactor
- [ ] release 0.1.0
- [ ] imx map
- [ ] imx report
- [ ] imx graph

--8<-- [end:main]

--8<-- [start:design]
## Design
todo

--8<-- [end:design]

--8<-- [start:contributing]

# Contributing
Contributions welcome! For more information on the design of the library, see design.

### Installation
todo

 - make install
 - optional dependency

## Contributing guide.

Make an effort to test each bit of functionality you add. Try to keep it simple. But first we need to add missing test and refactor code. 

The package will be used by end users so every public methode and class should have doc strings and examples. We use mkdocs to manage and publish documentation, we plan to make md files after finshing the alpha release.

### CI-CD github workflow
todo

### Requirements
We use a `pyproject.toml` to manage requirements that can be build by a newer build backend.
run `pip install .[dev, mkdocs]` or leave out any dependency option you want.

Dependencies have to be added to pyproject.toml by hand. We use flit as a build-backend and for managing (optional) dependencies, to build a local python wheen use `build_wheel`
 <!-- Todo: migrate to poetry: poetry as a build backend https://python-poetry.org/ -->

### Build and Test
Code quality checks and testing needs to be passed and will be checked by a git pre hook on every commit and in the pipeline. If code wont pass it won't commit! (warning stil a todo!)

Git-hooks will be set by pre-commit framework, adjust .pre-commit-config.yaml and make sure to install `pre-commit install` after adjustment. (warning stil a todo!)

We use make for quality of life: 

- pytest for testing, manual by `make test` in a console.
- flake8 and black for linting, manual by `make lint` in a console. <!-- todo: migrate to ruff to gain some rust speed on linting -->
- mypy for typechecking, manual by `make typecheck` in a console.
- isort for sorting imports, manual by `make format` in a console.
 

### Versioning
This library follows Semantic Versioning, every successful PR will get a new build id. Version can have a dev, alpha or beta releases state.

We use bumpversion for changing the version, version can be found in the `setting.cfg` and the `__init__.py` of the pyImx module:

  - bumpversion-build, manual and in (nightly) build `make bumpversion-build`
  - bumpversion-patch, manual `make bumpversion-patch`
  - bumpversion-minor, manual `make bumpversion-minor`
  - bumpversion-major, manual `make bumpversion-major`

--8<-- [end:contributing]

# License
MIT License

See LICENSE

--8<-- [start:credits]

##  Projects used in this project
- [make](https://www.gnu.org/software/make/manual/make.html)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [black](https://github.com/psf/black)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [iSort](https://github.com/PyCQA/isort)
- [bumpversion](https://github.com/peritus/bumpversion)
- [flit](https://flit.pypa.io/en/latest/)
- [mkdocs](https://www.mkdocs.org/)
- [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- ....

--8<-- [end:credits]