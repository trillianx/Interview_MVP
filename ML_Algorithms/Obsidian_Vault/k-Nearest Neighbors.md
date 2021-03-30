# K Nearest Neighbors

The k-Nearest Neighbors algorithm (kNN) is a [[supervised]] machine learning algorithm that can be used to solve both [[classification]] and [[regression]] problems. kNN makes use of [[distance]]. 

## How Does it Work? 

Let's assume the goal is to find the label of a query example. The kNN algorithm works in the following way: 

1. We initialize the number of neighbors, $k$. This is the value passed by the user. 
2. For each observation in the dataset we: 
	1. Find the distance between the observation and the query example.
	2. Add the distance computed to an array of distances
3. Repeat step 2 until you have run through all of the observations in the dataset.
4. Sort the distances in ascending order by using `np.argindex()` to get the indexes of the sorted array.
5. Subset the first $k$ indexes from the array of distances. 
6. Get the corresponding labels of these indexes.
7. Find the most common label among these labels. 
8. Return the most common label. 

The returned label will be the lable of the query example. 

## What is the Cost Function? 

kNN algorithm does not use a cost function as it is not trained. So, there is no [[optimization]] done. However, in the classification settings [[confusion matrix]] and other classification metrics such as [[mean error]] can be used to determine how accurate the model is. 

## What are the Hyperparameters?

There are two: $k$, which is the number of nearest neighbors and the distance metric. By default the distance metric is [[euclidean distance]]. However, other distance metrics can be used. The best value of the [[hyperparameter]], $k$, is determined by trying our multiple values of $k$ and seeing which $k$ gives the lowest mean error. However, care must be taken to not overfit the data. 

In general, use the smallest $k$ value that gives the lowest mean error. 

> When  is small, it tends to overfit while when is large, it underfits the data. For example, when , $k=1$, the model overfits the data while when $k=100$, it may underfit the data.

> When performing classification, if there are only two classes, $k$ is often chosen to be odd to break the tie.

> [[scaling]] and [[normalization]] is important as is the case with any algorithm that uses distances.

## What are the Strengths and Weaknesses?

**Strengths**
* Easy to understand and implement
* No need to fit, tune, and make additional assumption
* Works for both classification and regression

**Weakensses**

* Does not work well with high dimensional data. Typical of algorithms that use distances. 
* When the data are too large, kNN tends to slow dow as it measures distances to each and every observation every time it is run. 
* kNN does not work with categorical data as there are no distances.

## Where is kNN used? 

kNN is often used for recommendations. 

## kNN for Regression

kNN for regression works by finding the mean of the $k$ nearest neighbors and assigning the mean value to the query example. So, if you pass N feature values in a constant interval over the whole range of the feature, you will get N predictions. You can then connect these points together toget a regression line. Note, however that the regression line will not be a straight line but something like this: 

![[Pasted image 20210319092230.png]]

[Image Source](https://towardsdatascience.com/the-basics-knn-for-classification-and-regression-c1e8a6c955)

## kNN in scikit-learn

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Get the data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data" 

# Assign colum names to the dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset to pandas dataframe
dataset = pd.read_csv(url, names=names)

# Preprocessing
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Split the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Run the kNN
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Create confusion matrix
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Compute the error rate: 
error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))
```

Use the plot of mean error vs k to find the optimal k value.