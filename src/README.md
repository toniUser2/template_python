# README

## TODO

- pip install -e . and setup file... what it is good for?
- improve pytest:
every module in pytest need this three lines... get rid of it...
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
- use following example: [https://github.com/rochacbruno/python-project-template]
- include ruff (checkout Flake8)

## Description

Trading algo

## Doku

| Used Library  | Link                                          |
| --------      | -------                                       |
| numpy         | [https://numpy.org/devdocs/user/index.html]   |

## User Guide

### Setup Project

```bash
# run project_generator_for_python.pyw or...
python -m venv myenv
./venv/Scripts/Activate.ps1
pip install -r .\requirements.txt
```

## Dev Guide

### Get finance data

...
