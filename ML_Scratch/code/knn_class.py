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
		print(distances)

		# Sort the distances in increasing order and return indexes
		k_idx = np.argsort(distances)[:self.k]
		print(k_idx)

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
	
