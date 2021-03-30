# K-Means

k-Means is an unsurpervised machine learning algorithm that is used for [[classification]]. The k-means clustering creates $k$ clusters that are user-defined. 

## How Does it Work? 

We are given a data set. The k-means clustering carries out the following steps: 

1. Assign $k$ cluster centroids at random location in the data space.
2. For an observation, compute the distance between the centroids and the observation. The distance measurement is often the [[euclidean distance]]. 
3. Assign the label of the centroid that is nearest to the observation. 
4. Repeat steps 2-3 for all observations. 
5. Compute the arithmetic mean value of each of the clusters. Assign these mean values to each of the corresponding centroids.
6. Repeat steps 2-5 until there is no change in the centroid positions.  

## What is the Cost Function? 
The k-means clustering does not use a cost function that needs to be minimized. Instead, it makes use of [[expectation-maximization]]. The **Expectation-Maximization (EM)** is a powerful algorithm that is used in variety of contexts within machine learning. The EM algorithm has the following two steps: 

* Update our expectation
* Maximize some fitness function

In the k-Means clustering context, the our expectation of "which points belong to a given cluster" are updated in every iteration while maximization is carried out by finding the location of the cluster center through the use of an arithmetic mean. 

## What are the Hyperparameters?

We can consider $k$ to be a tunable parameter. As this is a unsupervised learning algorithm, we do not know the optimum value of $k$. The optimal value of $k$ is determined by computing the inter-cluster variance. We plot the reduction of variance as a function of $k$ and then using the [[elbow method]] to determine which $k$ value is optimal for use. 

![[Pasted image 20210329174141.png]]

## What are the Strengths and Weaknesses?

**Strengths**

* Easy to use
* Very quick in predictions for small dataset
* Easy to interpret

**Weaknesses**
* The EM algorithm always improves the result but does not always find a best solution. 
* Use of initial guess of $k$
* Slow for large datasets as distance computation can take time
* Works best for linear cluster boundaries

## k-Means in scikit-learn

```python
# Get the data
from sklearn.datasets.samples_generator import make_blobs
X, y_true = make_blobs(n_samples=300,
                       centers=4,
                       cluster_std=0.60,
					   random_state=0)
					   
# Visualize the centers
plt.scatter(X[:, 0], X[:, 1], s=50);

# Do the fit
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

y_kmeans = kmeans.predict(X)

# Visualize the final result
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
```