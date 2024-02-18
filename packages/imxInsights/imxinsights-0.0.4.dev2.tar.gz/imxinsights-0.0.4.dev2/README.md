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

    The goal for `imxInsights` is to get information from imx, ***adding, deleting or mutating data is out of scope!***.
    imx v5.0.0 support only. 

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