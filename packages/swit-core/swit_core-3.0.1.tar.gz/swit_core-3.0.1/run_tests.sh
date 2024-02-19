#!/bin/sh

flake8
mypy .
python -m unittest discover -s tests