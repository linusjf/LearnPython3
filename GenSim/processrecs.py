#!/usr/bin/env python
import pprint

master_recs = ["Lumiere Technologies", "Mendes Metal", "Klapisch Aerospace"]

text_corpus = [
    "Equipment ONLY - Lumiere Technologies",
    "Lumiere Technologies",
    "Lumiere Tech, Inc.",
    "Mendes Metal SA - Central Office",
    "*** DO NOT USE *** Mendes Metal",
    "Mendes Metal, SA",
    "Ship to Klapisch Aerospace gmbh",
    "Klapisch Aero, gmbh Munich",
    "Klapisch Aerospace tech (use Klapisch Aero, gmbh Munich acct 84719482-A)",
]

stoplist = set("for a of the and to *** -".lower().split(" "))

texts = [
    [word for word in document.lower().split() if word not in stoplist] for document in text_corpus
]

from collections import defaultdict

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]

print("Processed corpus: \n")
pprint.pprint(processed_corpus)

from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
print("Dictionary : \n")
print(dictionary)
noOfFeatures = len(dictionary)

print("Tokens and ids \n")
pprint.pprint(dictionary.token2id)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
print("Bag of words for corpus: \n")
pprint.pprint(bow_corpus)

from gensim import models

# train the model
tfidf = models.TfidfModel(bow_corpus)

import Levenshtein
from gensim import similarities
from math import sqrt

index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=noOfFeatures)

for rec in master_recs:
    query_document = rec.lower().split()
    query_bow = dictionary.doc2bow(query_document)
    print(rec + " bag of words: \n")
    print(tfidf[query_bow])
    sims = index[tfidf[query_bow]]

    for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
        if score > 0.0:
            print(document_number, score)
            leven = Levenshtein.distance(rec.lower(), text_corpus[document_number].lower())
            print("Levenshtein score: " + str(leven))
            leven_score = 1 - leven / max(len(rec), len(text_corpus[document_number]))
            print("Levenshtein normalised score: " + str(leven_score))
            wt_score = (score + leven_score) / 2
            print("Mean Weighted score: " + str(wt_score))
            geom_wt_score = sqrt(score * leven_score)
            print("Geometric Weighted score: " + str(geom_wt_score))
            harmonic_wt_score = 1 / (1 / score + 1 / leven_score)
            print("Harmonic Weighted score: " + str(harmonic_wt_score))
            print()
