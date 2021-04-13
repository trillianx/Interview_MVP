# Cost Functions 

Here we list out the cost functions used in Machine Learning. 

## Entropy

The [[entropy]] metric is commonly used by [[Decision Trees]] and [[Random Forest]] algorithms. Entropy, which originates from Thermodynamics, is used as a measure of impurity. A given set's impurity is zero if all the instances in the set belong to one class. The entropy equation is given by, 

$$
H_i = -\sum_{k=1}^n p_{i,k}log_2(p_{i,k})
$$

where $p_{i,k}$ is non-zero. The $p_{i,k}$ is the ratio of instances belonging to class $k$ in the $i$th node. In other words, we count the total number of instances belonging to a given class, $k$ and divide it by the total number of instances in $i$th node.

## Gini Index

Another most common purity metric used for CART is [[gini index]]. The Gini index is defined as, 

$$
G_i = 1 - \sum_{k=1}^n p_{i,k}^2
$$

where $p_{i,k}$ is non-zero. The $p_{i,k}$ is the ratio of instances belonging to class $k$ in the $i$th node.

