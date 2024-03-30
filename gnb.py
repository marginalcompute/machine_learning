import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.model_selection import train_test_split as split
from sklearn.metrics import accuracy_score as ac

data = pd.read_csv("tennisdata.csv")

X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

tmp = LabelEncoder()
X.Outlook = tmp.fit_transform(X.Outlook)
tmp = LabelEncoder()
X.Temperature = tmp.fit_transform(X.Temperature)
tmp = LabelEncoder()
X.Humidity = tmp.fit_transform(X.Humidity)
tmp = LabelEncoder()
X.Windy = tmp.fit_transform(X.Windy)

x_train, x_test, y_train, y_test = split(X, Y, test_size=0.2)
classifier = gnb()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

print("Accuracy:", classifier.score(x_test, y_test))

