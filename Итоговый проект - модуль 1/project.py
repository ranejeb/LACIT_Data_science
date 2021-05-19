"""
Используется модель на основе наивного байесовкого классификатора . Считать,
что условное распределение признаков является мультиномиальным распределением

В качестве входных данных выступают наборы из пяти признаков.
Два первых признака принимают значения из множества {0, 1}.
Три других –– из множества {0, 1, 2}.
Результатом является целое неотрицательное число меньшее 3.

"""

from math import log
from collections import defaultdict

def train(samples):
    classes, freq = defaultdict(lambda:0), defaultdict(lambda:0)
    for feats, label in samples:
        classes[label] += 1                 
        for feat in feats:
            freq[label, feat] += 1          

    for label, feat in freq:                
        freq[label, feat] /= classes[label]
    for c in classes:                       
        classes[c] /= len(samples)

    return classes, freq                    

def classify(classifier, feats):
    classes, prob = classifier
    return min(classes.keys(),              
        key = lambda cl: -log(classes[cl]) + \
            sum(-log(prob.get((cl,feat), 10**(-7))) for feat in feats))