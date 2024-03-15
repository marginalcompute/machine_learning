#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.model_selection  import train_test_split
from sklearn.neighbors import KNeighborsClassifier as kn
from sklearn import datasets


# In[55]:


iris = datasets.load_iris()


# In[54]:


x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size = 0.1)


# In[ ]:


for i in range(1, 9):
    classifier = kn(n_neighbors = i)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    print("Accuracy for i:",i,"is ", classifier.score(x_test, y_test))

