[TOC]



# Machine Learning From Scratch

My notes include writing well-known ML algorithms from scratch. These are often asked in coding interviews. I will start by first defining the algorithm. Then go into the steps of the algorithm and finally write a code to run the algorithm. The code has been taken from the following YouTube videos: 

*   [Python Engineer](https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA)

## kNN 

**Definition**

The kNN algorithm is used in classification problems. The kNN algorithm does not learn from the data instead it uses a distance metric, often Eucliedian Distance, to determine whether an observation belongs to a certain group or not. 

**Algorithm Steps**

The kNN algorithms follows these steps: 

1.  Measure distances from the new point's position to all other points in the dataset. use the L2-norm
2.  Sort the distances increasing order
3.  Take the top k points
4.  Take the mode of their labels
5.  Assign the label to the new point

For $n$ dimensions, the Euclidean distance is given by: 
$$
d = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}
$$
where $(q_i, p_i)$ are the pair positions of a point. When $n= 2$, we would have: 
$$
d = \sqrt{(q_1 - p_1)^2 + (q_2-p_2)^2}
$$
**Algorithm**

```python
import numpy as np
from collections import Counter

class knn():
	def __init__(self, k=3):
		self.k = k

	def fit(self, X, y):
		self.X_train = X
		self.y_train = y

	def predict(self, X):
		# Pass the X_test to the predict helper function
		# one row at a time
		y_pred = [self._predict(x) for x in X]
		return np.array(y_pred)

	def _predict(self, x):
		# This helper function takes one row of the X_test
		# computes the distances to each X_train, 
		# finds the most common and returns it

		# Compute the distances:
		distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]
		# Sort the distances in increasing order and return indexes
		k_idx = np.argsort(distances)[:self.k]
		# Extract the labels corresponding to the indexes:
		k_labels = self.y_train[k_idx]

		# Find most common class label
		most_common = Counter(k_labels).most_common(1)
		return np.array([most_common[0][0]])

	def _euclidean_distance(self, x1, x2):
		return np.sqrt(np.sum((x1 - x2)**2))
    
if __name__ == '__main__':
	from sklearn import datasets
	from sklearn.model_selection import train_test_split
	iris = datasets.load_iris()
	X, y = iris.data, iris.target
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)
	clf = knn()
	X_train = X_train[:5]
	clf.fit(X_train, y_train)
	X_test = X_test[:2]
	predictions = clf.predict(X_test)
	print(predictions)
```

## K-means

**Definition**

The k-Means is a unsupervised learning algorithm that is used to classify observations into multiple clusters. The number of clusters is based on the user-defined number, which is $k$. 

**Algorithm Steps**

1.  We start by randomly assigning $k$ cluster centers. 
2.  For each observation, we measure the distance between the observation and the cluster centroid. This is often done using Euclidean distance.
3.  Assign the nearest point to the given cluster
4.  Go through each observation by repeating steps 2 and 3
5.  Once we are done with all observations, we measure the mean of each cluster.
6.  We assign the position of each centroid equal to that of the mean value.
7.  We measure the variance of each cluster and note the positions of each cluster and the total variance.
8.  Repeat steps 2-7 number of times equal to the user-defined value or the cluster positions do not change.

Once we done, we output the positions of the clusters that resulted in the lowest cluster variance. 

