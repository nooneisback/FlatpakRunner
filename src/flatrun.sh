#!/bin/bash

script_name=$0
parent_name=$(dirname "$0")
python "$parent_name"/flatrun.py "$@"