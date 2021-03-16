[TOC]



# Machine Learning Algorithms

Here I include a list of ML algorithms that one should know when preparing for ML interviews. The algorithms are structured such that you can quickly and eloquently state: 

1.  What is it?
2.  How does it work?
3.  What is the cost function?
4.  What are the hyperparameters?
5.  What are its strenghts?
6.  What are its weaknesses?
7.  Where it is used?
8.  Final Note



## k-Nearest Neighbors

**What is it?**

The k-Nearest Neighbors algorithms (kNN) is a supervised ML algorithm that can be used to solve both classification and regression problems. 

**How does it work?**

The kNN works in the following way: 

1.  Initialize k to be the chosen number of neighbors
2.  For each observation in the dataset:
    1.  Calculate the distance (e.g. Euclidean, Manhattan) between the observation and the query example. The query example is unknown and we wish to either know the label (classfication) or value (regression). 
    2.  Add the distance to a list of distances
3.  Once you are gone through all the observations, sort the list in increasing order and find the indices of the sorted list.
4.  Take the first k indices and find their associated labels
5.  Depending on the type of the problem:
    1.  If the problem is regression, return the mean of the k values
    2.  if the problem is classification return the most common label among the k labels

**What is the cost function?**

kNN algorithm is not trained and therefore there is no cost function to be optimized. It simply runs, finds the k nearest neighbors, gets either the mean or the most common label and assigns that to the query example. However, you can select a cost function, which would be RSS for regression or an index for a classification problem.  

**What are the hyperparameters?**

There is only one, k, which is the number of nearest neighbors. This hyperparameter is determined by trying our various k values such that the difference between predictions and actual values is small. 

>   When $k$ is small, it tends to overfit while when $k$ is large, it underfits the data. For example, when $k=1$, the model overfits the data while when $K=100$, it may underfit the data. 

>   When performing classification, if there are only two classes, $k$ is often chosen to be odd to break the tie.

>   Scaling and normalization is important as is the case with any algorithm that uses distances.

**What are the strengths?**

*   Easy to understand and implement
*   No need to fit, tune, or make additional assumptions
*   Works for both classification and regression

**What are the weaknesses?**

*   The algorithm slows down and the number of observations increase

**Where is kNN used?**

*   Recommendations

**Final Note**

The use of kNN for regression is quite different than linear regression. In the case of regression, kNN simply finds points that are closest to query example and returns the mean of k nearest neighbors. If you wish to create a "linear" looking line, you will need to pass the features and then connect the output of the kNN, which would be the mean of k points. The result will look something like this: 

<img src="Database_of_ML_Algorithms.assets/image-20210315174917489.png" alt="image-20210315174917489" style="zoom:50%;" />

[Source](https://towardsdatascience.com/the-basics-knn-for-classification-and-regression-c1e8a6c955)

Note that this is not exactly a straight line but it does a fair join in fitting the data. 