#!/bin/bash

cp antonio.mplstyle ~/.config/matplotlib/stylelib

python plots.py
pdflatex text.tex

evince text.pdf
