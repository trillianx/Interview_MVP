# AdaBoost

[[Adaboost]], which stands for **Adaptive Boosting** trains on the mistakes of its predecessor. Adaboost uses **stumps**, a root with two nodes as weak learners. It is based on the [[ensemble learning]] and [[Boosting]] technique. 

Let's take a closer look at Adaboost algorithm

1. Each observation in the training data is given a same weight, $w^{(i)}=1/N$, where $N$ is the total number of observations in the dataset. 
2. Now we train the stump and evaluate the number of observations that were correctly classified and those that were incorrectly classified. 
3. We update the weights of the observations that were incorrectly classified while leaving the observations weights as they were in step 1. The updated weights are done using the following equations: 

	![[Pasted image 20210330104328.png]]

	The weights are all divided by $\sum_{i=1}^m w^{(i)}$ to ensure the weights are normalized. Here $\alpha_j$ is the $j$th model's (weak learner's) weight. It is also used to compute the new weights of the observations. 

	$\eta$ is the **learning rate**, a hyperparameter. The value of $\alpha_j$ is higher if the weak learner makes less mistakes and smaller if it makes more mistakes. The value of  $\alpha_j$ computed using the following equation: 

	![[Pasted image 20210330104615.png]]

	where $r_j$ is the weighted error rate for the $j$th weak learner. In other words, it is simply the ratio of weights of observations the weak learner got wrong over the total sum of weights. This is given by, 

	![[Pasted image 20210330104719.png]] 
1.  With updated weights, we repeat steps 2-3 until we go through all the stumps. 

To make predictions, Adaboost simply uses the predictions from each of the stumps, multiplies each predictions by their weak learner's weights $\alpha_j$ and outputs the most common class in a classification setting: 

![[Pasted image 20210330105546.png]]

Here $N$ are the number of weal learners used. 

## Adaboost in Scikit-Learn

Here is an example of Adaboost classifier that uses 200 stumps. 

```python
ada_clf = AdaBoostClassifier(
				DecisionTreeClassifier(max_depth=1),
                n_estimators=200,
                algorithm='SAMME.R'
                learning_rate=0.5
)

ada_clf.fit(X_train, y_train)
```

> If your adaboost ensemble is overfitting the training set, you can try reducing the number of estimators or more strongly regularizing the base estimator, the weak learner. 

