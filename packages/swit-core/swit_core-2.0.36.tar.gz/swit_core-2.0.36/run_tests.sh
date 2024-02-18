#!/bin/sh

flake8
pyright .
python -m unittest discover -s tests