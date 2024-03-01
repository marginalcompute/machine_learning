import numpy as np
import pandas as pd
from math import log


def entropy(total, positive):
    pos = positive/total
    neg = (total - positive)/total
    try:
        return -(pos)*log(pos, 2) -(neg)*log(neg, 2)
    except:
        return 0


def gain(S, col, atr, target):
    entropies = []
    for i in range(len(atr)):
        pos = 0
        for j in range(len(col)):
            if atr[i] == col[j]:
                if target[j] == "Yes":
                    pos += 1
        tmp = (round(entropy(col.count(atr[i]), pos), 4))
        tmp = (col.count(atr[i]) / len(col)) * tmp
        entropies.append(tmp)
    return S - sum(entropies)


# Extracting data from csv
data = pd.read_csv("dataset3.csv")
tmp = np.array(data)[:,:-1] # gives you the last coloumn
target = list(np.array(data)[:,-1]) # array without last coloumn

# Calculating Toal Entropy
pos = target.count("Yes")
total = len(target)
S = round(entropy(total, pos), 4)

# Making column list from numpy array
cols = []
for i in range(len(tmp[0])):
    cols.append(list(np.array(data)[:,i]))
    
# Getting unique attributes from each column
atr = [[] for i in range(len(cols))]
for i in range(len(cols)):
    for j in range(len(cols[i])):
        if cols[i][j] not in atr[i]:
            atr[i].append(cols[i][j])

# Claculating final gains for each column
ans = []
for i in range(len(cols)):
    ans.append(round(gain(S, cols[i], atr[i], target), 4))
ans
