# Decision Trees
Decision tree is a [[supervised learning]] and [[non-parametric]] algorithm used for [[classification]] and [[regression]] problems. The decision tree makes use of the binary tree data structure. It splits the feature space on a given metric dictated by the type of the problem. 

## How Does it Work?

To understand how a decision tree works, we will need to consider the classication and regression settings differently. 

### Classification
The decision tree, a binary tree, works in the following way: 

1. We starts at the **root**. Here we have all of the data. 
2. We find the best feature and best value to use to split the data. The optimal feature and threshold value are found by minimizing the cost function. This is performed through a greedy search algorithm. 
3. The tree will then create exactly two children. Children that are also parents are called **internal nodes**. 
4. For each node, steps 2-3 and repeated. 
5. The recursive iteration ends when:
	1.  The children have the lowest entropy and therefore cannot be split. Such children are called **leaf nodes**. 
	2.  A stopping criteria is reached. 
6.  At each of the leaf nodes, the most common label is found and that label is set for that leaf. 
7.  The predictions are made by following the decision at each node until one reaches the leaf node. The label at the leaf node is then read as the prediction for a given example observation. 


### Regression
A decision used for regression follows the same process as it does for classification. The only place where a regression tree differs from a classification tree is at the leaf node. At the leaf node, a regression decision tree computes the mean value of all the instances rather than the mode as it is done in the classification. 

## What is the Cost Function?
The decision trees algorithm makes use of either the [[entropy]] or the [[gini index]]. At each node, the best feature, $k$ and threshold value, $t_k$, is found by minimizing the cost function: 

![[Pasted image 20210329200511.png]]

where $m$ is the total number of instances in the dataset. 

## What are the Hyperparmeters? 
A decision tree algorthm has a lot of hyperparameters. These hyperparameters are used as a stopping criteria or restricting the tree from overfitting the data. These parameters are used for regression and classification. These hyperparameters are: 

*   `min_samples_split` - Minimum number of samples a node must have before it can split
*   `min_samples_leaf` - Minimum number of samples a leaf node must have
*   `min_weight_fraction_leaf` - This is the same as `min_samples_leaf` but expression as a fraction of total number of weighted instances
*   `max_leaf_nodes` - The maximum number of leaf nodes
*   `max_features` - The maximum number of features that are evaluated for splitting at each node

>In general, **increasing** `min_*` hyperparameters or **reducing** `max_*` hyperparameters will regularize the model. 

### Pruning

Another way to restrict a decision tree from overfitting is the use pruning. In pruning a node is deleted if: the children of this node provides no statistically significant improvement in the purity. The statistical significance is performed using the $\chi^2$ test. 

## What are the Strengths and Weaknesses?
**Strengths**

* Fast to fit and predict
* Easy to interpret
* Works for both linear and non-linear data

**Weaknesses**
* Has the tendency to overfit
* Work well when the decision boundaries are orthogonal
* Sensitive to small variation in the data (this goes with the first point)

Here's an example where the decision tree works best for orthogonal boundaries. The image on the left can easily be divided as the boundary is perpendicular to the x-axis. The figure on the right is simply rotated by 45 degrees resulting in a zigzag decision boundary. The model on the right will not generalize well. We can avoid this by using a [[PCA]]. 

## Where is Decision Tree Used?
These are not used. Instead, more robust version, [[Random Forest]] is used. 

## Decision Tree in Scikit-Learn

Here's an example of a decision tree classification: 

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

# Petal Length and Petal Width
X = iris.data[:, 2:]
y = iris.target

# Train a Tree
tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)

# Make a prediction on a single observation:
tree_clf.predict([[5.0, 1.5]])

> [[1]]

# Finding all the probabilities of classes: 
tree_clf.predict_proba([[5.0, 1.5]])

> array([[0.        , 0.90740741, 0.09259259]])
```

The `predict_proba()` gives the probabilities of all the classes in the dataset. In the above example it gave probabilities of each of three class in the Iris Dataset. 

Here's an example of classification with and without regularization: 

![[Pasted image 20210329202721.png]]

Here is an example of decision tree regression: 

```python
from sklearn.tree import DecisionTreeRegressor

tree_reg = DecisionTreeRegressor(max_depth=2)
tree_reg.fit(X, y)

tree_reg.predict([[5.0, 1.5]])
```

Here is an exampe of regression tree with and without regularization:

![[Pasted image 20210329202905.png]]

In the regularization image, you can clearly see how the decision tree computes the mean value of the dataset.