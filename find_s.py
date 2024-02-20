import numpy as np
import pandas as pd


data = pd.read_csv("dataset1.csv")
sample = np.array(data)[1:,:-1]  # Removes the header and last coloumn of data
target = np.array(data)[1:,-1]  # Removes the header and gives the last coloumn


def train(sample, target):
    # Initializing specific_hypothesis
    for i in range(len(target)):
        if target[i] == "Yes":
            specific_hypothesis = list(sample[i])
            break

    # Tuning specific_hypothesis
    for i in range(len(sample)):
        if target[i] == "Yes":
            for j in range(len(specific_hypothesis)):
                if sample[i][j] != specific_hypothesis[j]:
                    specific_hypothesis[j] = '?'

    return specific_hypothesis


def predict(sample, specific_hypothesis):
    for i in range(len(sample)):
        if specific_hypothesis[i] != '?' and specific_hypothesis[i] != sample[i]:
            return False
    return True


specific_hypothesis = train(sample, target)
print("Specific Hypothesis: ", specific_hypothesis)
example = ["Night", "Sunny", "Moderate", "Yes", "Normal", "Low"]
ans = predict(example, specific_hypothesis)
print("Prediction for ", example, " is ", ans)
