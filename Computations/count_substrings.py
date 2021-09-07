#!/usr/bin/env python
# -*- coding: utf-8 -*-

gene = 'AGTCAATGGAATAGGCCAAGCGAATATTTGGGCTACCA'

def freq(letter, text):
    counter = 0
    for i in text:
        if i == letter:
            counter += 1
    return counter/float(len(text))

def pairs(letter, text):
    counter = 0
    for i in range(len(text)):
        if i < len(text)-1 and \
               text[i] == letter and text[i+1] == letter:
            counter += 1
    return counter

def mystruct(text):
    counter = 0
    for i in range(len(text)):
        # Search for the structure from position i
        if text[i] == 'G':
            print('found G at', i)
            # Search among A and T letters
            j = i + 1
            while text[j] == 'A' or text[j] == 'T':
                print('next is ok:', text[j])
                j = j + 1
            print('ending is', text[j:j+2])
            if text[j:j+2] == 'GG':
                # Correct ending of structure
                counter += 1
                print('yes')
    return counter

print('frequency of C: %.1f' % freq('C', gene))
print('frequency of G: %.1f' % freq('G', gene))
print('no of pairs AA: %d' % pairs('A', gene))
print('no of structures: %d' % mystruct(gene))
