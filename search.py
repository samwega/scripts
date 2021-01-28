#!/usr/bin/python3
# simple rofi/dmenu websearch using elinks
# ddg stands for duckduckgo. It is possible to replace it with other search engines.

from sys import argv, exit
import os

# User settings:
TERM = 'alacritty'

os.system(f"exec {TERM} -e elinks ddg:'{argv[1:]}'")
