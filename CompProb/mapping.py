#!/usr/bin/env python
# -*- coding: utf-8 -*-
import comp_prob_inference as cpi

"""
Probability mappings
"""

prob_space = {"sunny": 1 / 2, "rainy": 1 / 6, "snowy": 1 / 3}

W_mapping = {"sunny": "sunny", "rainy": "rainy", "snowy": "snowy"}
I_mapping = {"sunny": 1, "rainy": 0, "snowy": 0}

random_outcome = cpi.sample_from_finite_probability_space(prob_space)
W = W_mapping[random_outcome]
print(W)
I = I_mapping[random_outcome]
print(I)

W_table = {"sunny": 1 / 2, "rainy": 1 / 6, "snowy": 1 / 3}
I_table = {0: 1 / 2, 1: 1 / 2}

W = cpi.sample_from_finite_probability_space(W_table)
print(W)
I = cpi.sample_from_finite_probability_space(I_table)
print(I)
