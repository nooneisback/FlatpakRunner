#!/bin/bash
parent_name=$(dirname "$0")
python "$parent_name"/flatrun.py "$@"
