#!/usr/bin/env python
"""
Hashwordsserial.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : hashwordsserial
# @created     : Sunday Nov 19, 2023 19:04:52 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of hashing a word list serially
from hashlib import sha512
import timeit


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


def entry():
    """entry point"""
    # load a file of words
    path = '1.1millionwordlist.txt'
    words = load_words(path)
    print(f'Loaded {len(words)} words from {path}')
    # hash all known words
    known_words = {hash_word(word) for word in words}
    print(f'Done, with {len(known_words)} hashes')


def main():
    """Main function"""
    entry()


if __name__ == '__main__':
    start = timeit.default_timer()
    print("The start time is :", start)
    main()
    print("The difference of time is :",
          timeit.default_timer() - start)
