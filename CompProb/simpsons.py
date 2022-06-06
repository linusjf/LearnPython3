#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simpsons_paradox_data import *

print("Gender='Female',Dept='C',Admission='Admitted')")
print(joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']])

joint_prob_gender_admission = joint_prob_table.sum(axis=1)

print("Marginal probability matrix for Gender + Admission")
print(joint_prob_gender_admission)

print("Marginal probability for Gender = Female")
female_only = joint_prob_gender_admission[gender_mapping['female']]
print(female_only)

print("Probability for Female + Admitted")
prob_female_admitted = joint_prob_gender_admission[gender_mapping['female'], admission_mapping['admitted']]
print(prob_female_admitted)
prob_admitted_given_female = prob_female_admitted / np.sum(female_only)

print("Probability for Admitted|Female")
print(prob_admitted_given_female)
