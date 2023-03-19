#!/usr/bin/env python
"""
Githubhungarian.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : githubhungarian
# @created     : Sunday Mar 19, 2023 11:45:53 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from hungarian_algorithm import algorithm  # type: ignore

G = {
    "Ann": {"RB": 3, "CAM": 2, "GK": 1},
    "Ben": {"LW": 3, "S": 2, "CM": 1},
    "Cal": {"CAM": 3, "RW": 2, "SWP": 1},
    "Dan": {"S": 3, "LW": 2, "GK": 1},
    "Ela": {"GK": 3, "LW": 2, "F": 1},
    "Fae": {"CM": 3, "GK": 2, "CAM": 1},
    "Gio": {"GK": 3, "CM": 2, "S": 1},
    "Hol": {"CAM": 3, "F": 2, "SWP": 1},
    "Ian": {"S": 3, "RW": 2, "RB": 1},
    "Jon": {"F": 3, "LW": 2, "CB": 1},
    "Kay": {"GK": 3, "RW": 2, "LW": 1, "LB": 0},
}
print(algorithm.find_matching(G, matching_type="max", return_type="list"))
print(algorithm.find_matching(G, matching_type="max", return_type="total"))

H = {
    "A": {"#191": 22, "#122": 14, "#173": 120, "#121": 21, "#128": 4, "#104": 51},
    "B": {"#191": 19, "#122": 12, "#173": 172, "#121": 21, "#128": 28, "#104": 43},
    "C": {"#191": 161, "#122": 122, "#173": 2, "#121": 50, "#128": 128, "#104": 39},
    "D": {"#191": 19, "#122": 22, "#173": 90, "#121": 11, "#128": 28, "#104": 4},
    "E": {"#191": 1, "#122": 30, "#173": 113, "#121": 14, "#128": 28, "#104": 86},
    "F": {"#191": 60, "#122": 70, "#173": 170, "#121": 28, "#128": 68, "#104": 104},
}
print(algorithm.find_matching(H, matching_type="min", return_type="list"))
print(algorithm.find_matching(H, matching_type="min", return_type="total"))
