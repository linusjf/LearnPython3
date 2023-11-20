#!/usr/bin/env python
"""
Hashwordsparallel.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hashwordsparallel
# @created     : Sunday Nov 19, 2023 19:29:04 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of hashing a word list concurrently
# from math import ceil
from hashlib import sha512
from concurrent.futures import ProcessPoolExecutor
import timeit


def hash_word(word):
    """hash one word using the SHA algorithm"""
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data = word.encode("utf-8")
    # hash the word
    hash_object.update(byte_data)
    # get the hex hash of the word
    return hash_object.hexdigest()


def load_words(path):
    """load a file of words"""
    # open the file
    with open(path, encoding="UTF-8") as file:
        # read all data as lines
        return file.readlines()


def main():
    """entry point"""
    # load a file of words
    path = "1.1millionwordlist.txt"
    words = load_words(path)
    print(f"Loaded {len(words)} words from {path}")
    # create the process pool
    with ProcessPoolExecutor(4) as executor:
        # select a chunk size
        # chunksize = ceil(len(words) / 4)
        # create a set of word hashes
        known_words = set(executor.map(hash_word, words, chunksize=10000))
    print(f"Done, with {len(known_words)} hashes")


if __name__ == "__main__":
    start = timeit.default_timer()
    print("The start time is :", start)
    main()
    print("The difference of time is :", timeit.default_timer() - start)
