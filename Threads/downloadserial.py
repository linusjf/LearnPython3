#!/usr/bin/env python
"""
Downloadserial.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : downloadserial
# @created     : Thursday Nov 16, 2023 20:27:53 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# download document files and save to local files serially
from os import makedirs
from os.path import basename
from os.path import join
from urllib.request import urlopen
from urllib.error import URLError


def download_url(url):
    """download a url and return the raw data, or None on error"""
    try:
        # open a connection to the server
        with urlopen(url, timeout=3) as connection:
            # read the contents of the html doc
            return connection.read()
    except URLError as ex:
        # bad url, socket timeout, http forbidden, etc.
        print(ex)
        return None


def save_file(url, data, path):
    """save data to a local file"""
    # get the name of the file from the url
    filename = basename(url)
    # construct a local path for saving the file
    outpath = join(path, filename)
    # save to file
    with open(outpath, 'wb') as file:
        file.write(data)
    return outpath


def download_and_save(url, path):
    """download and save a url as a local file"""
    # download the url
    data = download_url(url)
    # check for no data
    if data is None:
        print(f'>Error downloading {url}')
        return
    # save the data to a local file
    outpath = save_file(url, data, path)
    # report progress
    print(f'>Saved {url} to {outpath}')


def download_docs(urls, path):
    """download a list of URLs to local files"""
    # create the local directory, if needed
    makedirs(path, exist_ok=True)
    # download each url and save as a local file
    for url in urls:
        download_and_save(url, path)


# python concurrency API docs
URLS = ['https://docs.python.org/3/library/concurrency.html',
        'https://docs.python.org/3/library/concurrent.html',
        'https://docs.python.org/3/library/concurrent.futures.html',
        'https://docs.python.org/3/library/threading.html',
        'https://docs.python.org/3/library/multiprocessing.html',
        'https://docs.python.org/3/library/multiprocessing.shared_memory.html',
        'https://docs.python.org/3/library/subprocess.html',
        'https://docs.python.org/3/library/queue.html',
        'https://docs.python.org/3/library/sched.html',
        'https://docs.python.org/3/library/contextvars.html']
# local path for saving the files
PATH = 'docs'
# download all docs
download_docs(URLS, PATH)
