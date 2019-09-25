#!/usr/bin/env python3
"""Zipping it up."""
from os import path
from shutil import make_archive
from zipfile import ZipFile


# Check if file exists
if path.exists("career.guru99.txt"):
    # get the path to the file in the current directory
    SRC = path.realpath("guru99.txt")
    # now put things into a ZIP archive
    ROOT_DIR, TAIL = path.split(SRC)
    make_archive("guru99 archive", "zip", ROOT_DIR)
    # more fine-grained control over ZIP files
    with ZipFile("testguru99.zip", "w") as newzip:
        newzip.write("career.guru99.txt")
        newzip.write("guru99.txt.bak")
