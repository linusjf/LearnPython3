#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Probabilities with Events and Code
"""


def prob_of_event(event, prob_space):
    total = 0
    for outcome in event:
        total += prob_space[outcome]
    return total


prob_space = {"sunny": 1 / 2, "rainy": 1 / 6, "snowy": 1 / 3}
rainy_or_snowy_event = {"rainy", "snowy"}
print(prob_of_event(rainy_or_snowy_event, prob_space))
