import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv")
pizza_diameter = np.array(data)[:,:1]
price = np.array(data)[:,-1]

x = [i[0] for i in pizza_diameter]
y = list(price)

mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)

deviation_x = [i-mean_x for i in x]
deviation_y = [i-mean_y for i in y]

product_deviation = []
for i in range(len(x)):
    product_deviation.append(deviation_x[i] * deviation_y[i])

square_deviation_x = [i**2 for i in deviation_x]
slope = sum(product_deviation) / sum(square_deviation_x)
intercept = mean_y - (slope * mean_x)

X = [i for i in range(-1, 20)]
Y = [slope*i + intercept for i in X]

plt.plot(X, Y)
plt.scatter(x, y)
plt.show
