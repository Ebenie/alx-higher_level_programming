#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""

from sys import argv
from os import path
from json import dump, load
from collections import deque

filename = "add_item.json"

if path.exists(filename):
    with open(filename, 'r') as f:
        my_list = load(f)
else:
    my_list = []

my_list.extend(argv[1:])
with open(filename, 'w') as f:
    dump(my_list, f)

