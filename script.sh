#!/bin/bash
python plots.py
pdflatex text.tex

evince text.pdf
