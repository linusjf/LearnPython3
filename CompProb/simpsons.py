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

print("Marginal probability for Gender = Male")
male_only = joint_prob_gender_admission[gender_mapping['male']]
print(male_only)

print("Probability for Female + Admission")
prob_female_admission = joint_prob_gender_admission[gender_mapping['female'], ]
print(prob_female_admission)
prob_admission_given_female = prob_female_admission / np.sum(female_only)

print("Probability for Male + Admission")
prob_male_admission = joint_prob_gender_admission[gender_mapping['male'], ]
print(prob_male_admission)
prob_admission_given_male = prob_male_admission / np.sum(male_only)

print("Probability for Admission|Female")
print(prob_admission_given_female)

prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print("Probability for Admission|Female (Dict)")
print(prob_admission_given_female_dict)

print("Probability for Admission|Male")
print(prob_admission_given_male)

prob_admission_given_male_dict = dict(zip(admission_labels, prob_admission_given_male))
print("Probability for Admission|Male (Dict)")
print(prob_admission_given_male_dict)
