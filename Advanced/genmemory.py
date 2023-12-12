#!/usr/bin/env python
"""
Genmemory.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : genmemory
# @created     : Tuesday Dec 12, 2023 10:20:30 IST
# @description :
https://www.linkedin.com/posts/rajeev-kumar-34201228_generators-in-python-create-data-on-the-fly-activity-7139333493704085504-P-r3
# -*- coding: utf-8 -*-'
######################################################################
"""
import os
import time
import secrets
import psutil


def memory_usage_psutil():
    """Return memory usage in MB"""
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem


names = ["Amit", "Jack", "Jill", "Trisha", "Imam"]
subjects = ["Mathematics", "Science", "Economics", "Geography", "History"]
RECORDS = 1000000

print(f"Test for Records:{RECORDS}")
print("++++++++++ Test for Return Statement ++++++++")


def person_subject_list(num_people):
    """Return list of people"""
    result = []
    for i in range(num_people):
        person = {
                'id': i,
                "name": secrets.choice(names),
                "subject": secrets.choice(subjects)
                }
        result.append(person)
    return result


t1 = time.time()
persons = person_subject_list(RECORDS)
t2 = time.time()

print(f"Memory (Before): {memory_usage_psutil()} MB")
print(f"Took {(t2 - t1)} seconds")

print("++++++++++ Test for Yield Generator Statement ++++++++")


def person_subject_generator(num_people):
    """Yield generator of people"""
    for i in range(num_people):
        person = {
                'id': i,
                "name": secrets.choice(names),
                "subject": secrets.choice(subjects)
                }
        yield person


t1 = time.time()
persons = person_subject_generator(RECORDS)
t2 = time.time()

print(f"Memory (Before): {memory_usage_psutil()} MB")
print(f"Took {(t2 - t1)} seconds")
