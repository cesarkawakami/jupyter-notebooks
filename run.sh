#!/usr/bin/env bash

exec docker run --rm -it -p 8888:8888 -v "$(pwd):/home/jovyan/work" jupyter/scipy-notebook "$@"
