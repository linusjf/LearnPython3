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

print("Marginal probability for Admission = Admitted")
admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
print(admitted_only)

print("Probability Gender|Admission=Admitted")
prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
print(prob_gender_given_admitted)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print("Probability Gender|Admission=Admitted (Dict)")
print(prob_gender_given_admitted_dict)

female_and_A_only = joint_prob_table[gender_mapping['female'], department_mapping['A']]
print("Probability of female and department A")
print(female_and_A_only)
prob_admission_given_female_A = female_and_A_only/np.sum(female_and_A_only)
print("Probability Admission|Gender=Female & Dept=A")
print(prob_admission_given_female_A)
prob_admission_given_female_A_dict = dict(zip(admission_labels, prob_admission_given_female_A))
print("Probability Admission|Gender=Female & Dept=A (Dict)")
print(prob_admission_given_female_A_dict)

male_and_A_only = joint_prob_table[gender_mapping['male'], department_mapping['A']]
print("Probability of male and department A")
print(male_and_A_only)
prob_admission_given_male_A = male_and_A_only/np.sum(male_and_A_only)
print("Probability Admission|Gender=Male & Dept=A")
print(prob_admission_given_male_A)
prob_admission_given_male_A_dict = dict(zip(admission_labels, prob_admission_given_male_A))
print("Probability Admission|Gender=Male & Dept=A (Dict)")
print(prob_admission_given_male_A_dict)

female_and_B_only = joint_prob_table[gender_mapping['female'], department_mapping['B']]
print("Probability of female and department B")
print(female_and_B_only)
prob_admission_given_female_B = female_and_B_only/np.sum(female_and_B_only)
print("Probability Admission|Gender=Female & Dept=B")
print(prob_admission_given_female_B)
prob_admission_given_female_B_dict = dict(zip(admission_labels, prob_admission_given_female_B))
print("Probability Admission|Gender=Female & Dept=B (Dict)")
print(prob_admission_given_female_B_dict)

male_and_B_only = joint_prob_table[gender_mapping['male'], department_mapping['B']]
print("Probability of male and department B")
print(male_and_B_only)
prob_admission_given_male_B = male_and_B_only/np.sum(male_and_B_only)
print("Probability Admission|Gender=Male & Dept=B")
print(prob_admission_given_male_B)
prob_admission_given_male_B_dict = dict(zip(admission_labels, prob_admission_given_male_B))
print("Probability Admission|Gender=Male & Dept=B (Dict)")
print(prob_admission_given_male_B_dict)

female_and_C_only = joint_prob_table[gender_mapping['female'], department_mapping['C']]
print("Probability of female and department C")
print(female_and_C_only)
prob_admission_given_female_C = female_and_C_only/np.sum(female_and_C_only)
print("Probability Admission|Gender=Female & Dept=C")
print(prob_admission_given_female_C)
prob_admission_given_female_C_dict = dict(zip(admission_labels, prob_admission_given_female_C))
print("Probability Admission|Gender=Female & Dept=C (Dict)")
print(prob_admission_given_female_C_dict)

male_and_C_only = joint_prob_table[gender_mapping['male'], department_mapping['C']]
print("Probability of male and department C")
print(male_and_C_only)
prob_admission_given_male_C = male_and_C_only/np.sum(male_and_C_only)
print("Probability Admission|Gender=Male & Dept=C")
print(prob_admission_given_male_C)
prob_admission_given_male_C_dict = dict(zip(admission_labels, prob_admission_given_male_C))
print("Probability Admission|Gender=Male & Dept=C (Dict)")
print(prob_admission_given_male_C_dict)

female_and_D_only = joint_prob_table[gender_mapping['female'], department_mapping['D']]
print("Probability of female and department D")
print(female_and_D_only)
prob_admission_given_female_D = female_and_D_only/np.sum(female_and_D_only)
print("Probability Admission|Gender=Female & Dept=D")
print(prob_admission_given_female_D)
prob_admission_given_female_D_dict = dict(zip(admission_labels, prob_admission_given_female_D))
print("Probability Admission|Gender=Female & Dept=D (Dict)")
print(prob_admission_given_female_D_dict)

male_and_D_only = joint_prob_table[gender_mapping['male'], department_mapping['D']]
print("Probability of male and department D")
print(male_and_D_only)
prob_admission_given_male_D = male_and_D_only/np.sum(male_and_D_only)
print("Probability Admission|Gender=Male & Dept=D")
print(prob_admission_given_male_D)
prob_admission_given_male_D_dict = dict(zip(admission_labels, prob_admission_given_male_D))
print("Probability Admission|Gender=Male & Dept=D (Dict)")
print(prob_admission_given_male_D_dict)

female_and_E_only = joint_prob_table[gender_mapping['female'], department_mapping['E']]
print("Probability of female and department E")
print(female_and_E_only)
prob_admission_given_female_E = female_and_E_only/np.sum(female_and_E_only)
print("Probability Admission|Gender=Female & Dept=E")
print(prob_admission_given_female_E)
prob_admission_given_female_E_dict = dict(zip(admission_labels, prob_admission_given_female_E))
print("Probability Admission|Gender=Female & Dept=E (Dict)")
print(prob_admission_given_female_E_dict)

male_and_E_only = joint_prob_table[gender_mapping['male'], department_mapping['E']]
print("Probability of male and department E")
print(male_and_E_only)
prob_admission_given_male_E = male_and_E_only/np.sum(male_and_E_only)
print("Probability Admission|Gender=Male & Dept=E")
print(prob_admission_given_male_E)
prob_admission_given_male_E_dict = dict(zip(admission_labels, prob_admission_given_male_E))
print("Probability Admission|Gender=Male & Dept=E (Dict)")
print(prob_admission_given_male_E_dict)

female_and_F_only = joint_prob_table[gender_mapping['female'], department_mapping['F']]
print("Probability of female and department F")
print(female_and_F_only)
prob_admission_given_female_F = female_and_F_only/np.sum(female_and_F_only)
print("Probability Admission|Gender=Female & Dept=F")
print(prob_admission_given_female_F)
prob_admission_given_female_F_dict = dict(zip(admission_labels, prob_admission_given_female_F))
print("Probability Admission|Gender=Female & Dept=F (Dict)")
print(prob_admission_given_female_F_dict)

male_and_F_only = joint_prob_table[gender_mapping['male'], department_mapping['F']]
print("Probability of male and department F")
print(male_and_F_only)
prob_admission_given_male_F = male_and_F_only/np.sum(male_and_F_only)
print("Probability Admission|Gender=Male & Dept=F")
print(prob_admission_given_male_F)
prob_admission_given_male_F_dict = dict(zip(admission_labels, prob_admission_given_male_F))
print("Probability Admission|Gender=Male & Dept=F (Dict)")
print(prob_admission_given_male_F_dict)
