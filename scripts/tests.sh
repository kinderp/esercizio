#!/bin/bash
rm -rf test/datatype/__pycache__
rm -rf test/parser/__pycache__
python -m pytest
