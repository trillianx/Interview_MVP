# Bagging

Bagging in an [[ensemble learning]] technique where rather than using a single machine learning models, we use multiple copies of it. Bagging creates multiple [[Decision Trees]] and each decision tree is given a subset of observations created using [[bootstrap]]. The prediction is made by taking the average of all predictions from the trees in the case of [[regression]] or using the most common label in the case of [[classification]]. 

## How Does it Work? 

Bagging creates hundreds of subsets of training data using bootstrap. Then each decision tree is trained on this subset of data. Note that no bootstrap is performed on features, unlike [[Random_Forest]].

The figure below shows the gist of bagging technique: 

![[Pasted image 20210330091216.png]]

* When a subset of data is created randomly **with replacement**, it is called **Bagging**
* When a subset of data is created randomly **without replacement**, it is called **pasting**.

>The use of ensemble learning reduces variance as we take the average, we effectively take the average of the variance. The total variance in the ensemble is the sum of the variance of each algorithm divided by the total number of algorithms. This has no effect on the bias. Therefore, we are able to reduce variance by keeping the bias the same.

One advantage of bagging is that the randomness of bootstrap leaves out about 37% of the training data which is not used for training an algorithm. This 37% can then be used to test the performance of the algorithm. This is known as [[out-of-Bag Evaluation]]. In other words, we get to use the training set to test the algorithm without the need of test dataset (which we use anyway). 

## What is the Cost Function?

As bagging is a technique that takes an algorithm, makes multiple copies and trains on a boostrap subset of data, the cost function for bagging would be the cost function used for the given algorithm. In other words, if bagging uses a decision tree, the cost function would entropy, Gini index, or information gain. 

## What are the Hyperparameters? 

The hyperparameters are those of algorithm that bagging uses. However, when `bootstrap=True` is set, we have bagging while `bootstrap=False` results in pasting. 

## What are the Strengths and Weaknesses? 

**Strengths**

* Allows to lower the variance
* Easy to interpret
* Works great in multiprocessing

**Weaknesses**

* Trees tend to be identical
* Adding more trees may not improve performance

## Bagging in Scikit-Learn

Here is bagging using classifier: 

```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bag_clf = BaggingClassifier(
             DecisionTreeClassifier(),
             n_estimators=500,
             max_samples=100,
             bootstrap=True,
             n_jobs=-1,
			 oob_score=True
             )

bag_clf.fit(X_train, y_train)
y_pred = bag_clf.predict(X_test)

```

You will notice that we use `oob_score=True`. This will result in out of bag scores. 

The figure below shows the use of single decision tree and decision trees using bagging: 

![[Pasted image 20210330090933.png]]