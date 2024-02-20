import numpy as np
import pandas as pd


data = pd.read_csv("dataset1.csv")
sample = np.array(data)[1:,:-1]  # Removes the header and last coloumn of data
target = np.array(data)[1:,-1]   # Removes the header and gives the last coloumn


def train(sample, target):
    specific_hypothesis = list(sample[0]) # assumes first sample is positive
    num_atb = len(specific_hypothesis)
    generic_hypothesis = [['?' for i in range(num_atb)] for j in range(num_atb)]

    for i in range(len(sample)):
        if target[i] == "Yes":
            if specific_hypothesis != list(sample[i]):
                for j in range(num_atb):
                    if sample[i][j] != specific_hypothesis[j] and specific_hypothesis[j] != '?':
                        specific_hypothesis[j] = '?'
                        generic_hypothesis[j][j] = '?'
        else:
            for j in range(num_atb):
                if sample[i][j] != specific_hypothesis[j]:
                    generic_hypothesis[j][j] = specific_hypothesis[j]
                else:
                    generic_hypothesis[j][j] = '?'

    tmp = ['?' for _ in range(num_atb)]
    generic_hypothesis = [i for i in generic_hypothesis if i != tmp]

    return specific_hypothesis, generic_hypothesis


specific_hypothesis, generic_hypothesis = train(sample, target)
print(f"Specific Hypothesis: {specific_hypothesis}\nGeneric Hypothesis: {generic_hypothesis}")
