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

print("Probability for Female + Admission")
prob_female_admission = joint_prob_gender_admission[gender_mapping['female'], ]
print(prob_female_admission)
prob_admission_given_female = prob_female_admission / np.sum(female_only)

print("Probability for Admission|Female")
print(prob_admission_given_female)

prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print("Probability for Admission|Female (Dict)")
print(prob_admission_given_female_dict)
