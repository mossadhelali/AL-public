#!/usr/bin/bash


conda create -n al python=3.6

conda activate al

pip install -r requirements.txt

cd ../../

conda env config vars set PYTHONPATH=$PWD:$PATH

cd src/core/