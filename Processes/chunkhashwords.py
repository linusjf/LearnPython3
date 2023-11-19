#!/usr/bin/env python
"""
Chunkhashwords.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : chunkhashwords
# @created     : Sunday Nov 19, 2023 19:37:37 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of testing chunksize when hashing a word list concurrently
from math import ceil
from time import time
from hashlib import sha512
from concurrent.futures import ProcessPoolExecutor


def hash_word(word):
    """hash one word using the SHA algorithm"""
    # create the hash object
    hash_object = sha512()
    # convert the string to bytes
    byte_data = word.encode('utf-8')
    # hash the word
    hash_object.update(byte_data)
    # get the hex hash of the word
    return hash_object.hexdigest()


def load_words(path):
    """load a file of words"""
    # open the file
    with open(path, encoding='utf-8') as file:
        # read all data as lines
        return file.readlines()


def test_chunksize(words, size):
    """test a chunksize"""
    time1 = time()
    # create the process pool
    with ProcessPoolExecutor(4) as executor:
        # create a set of word hashes
        _ = set(executor.map(hash_word, words, chunksize=size))
    time2 = time()
    total = time2 - time1
    print(f'{size}: {total:.3f} seconds')


def main():
    """entry point"""
    # load a file of words
    path = '1.1millionwordlist.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    # test chunk sizes
    base = ceil(len(words) / 4)
    sizes = [len(words), base, 100000, 50000, 10000, 5000, 1000, 500]
    for size in sizes:
        test_chunksize(words, size)


if __name__ == '__main__':
    main()
