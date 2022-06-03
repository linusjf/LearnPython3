#!/usr/bin/env python
# -*- coding: utf-8 -*-
import comp_prob_inference as cpi

print(cpi.flip_fair_coin())
flips = cpi.flip_fair_coins(100)
cpi.plot_discrete_histogram(flips)
cpi.plt.savefig("flips.pdf")
