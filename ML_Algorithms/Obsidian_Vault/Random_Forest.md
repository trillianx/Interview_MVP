# Random Forest

A Random Forest is a [[supervised learning]] algorithm that makes use of  [[ensemble learning]] technique. Random forest is based on [[Bagging]] and is used for [[classification]] and [[regression]]. However, unlike bagging, Random Forest creates hundreds of [[Decision Trees]] by randomly sampling a subset of features at every node of a tree while using all of the training data for each decision tree. 

## How Does it Work? 

Random forest works just like how a decision tree works, with the exception of splitting on features. Rather than split on the same list of $m$ features at every node, random forest [[bootstrap]] $k$ features from a total of $m$ features. Note that boostrap is sampling random values *with replacement*. A decision tree is created based on this criteria until a stopping criteria is reached. 

The random forest then creates another tree based on the above description. In fact, it creates hundreds or thousands of such decision trees. Because each tree is created by a random set of features, each tree is independent of each other. **This results in higher bias and low variance resulting in a model that fits better. **

When the time comes to make predictions, each decision tree in the random forest outputs a prediction. In the classification setting, the most common label is taken to be the final prediction. In the regression setting, the mean value of all the predictions is taken to the final prediction.

> Sampling features results in even more feature diversity, trading more bias for a lower variance. 

## What are the Hyperparameters? 

A random forest has all of the hyperparameters of the [[Decision Trees]] and [[Bagging]]. In addition, the hyperparameter, `n_estimator` controls the number of decision trees a random forest can have. 

## What are the Strengths & Weaknesses? 

**Strengths**

* Fast to fit and predict. Works well with MapReduce
* Easy to interpret
* Have lower variance and high bias making them robust to changes in the data
* Able to deal with unbalanced and missing data
* Robust against outliers

**Weaknesses**

* Cannot predict beyond the range in the training data
* Tend to overfit noisy data
* Longer training period as it generates hundreds of trees


## Where is Random Forest Used? 

Random forest is used for both regression and classification problems. Another advantage of random forest is [[feature importances]]. Feature importances is frequency table that lists the features and the number of times these features were used to create decision trees. A feature that is most often used to split a feature is most important to explain the variance in the dataset. 

## Random Forest in Scikit-Learn

Here is an example of Random Forest: 

```python
from sklearn.ensemble import RandomForestClassifier

rnd_clf = RandomForestClassifier(
						n_estimators=500,
    					max_leaf=16,
    					n_jobs=-1
                        )

rnd_clf.fit(X_train, y_train)
y_pref_rf = rnd_clf.predict(X_test)

# Get Feature Importances
for name, score in zip(X['feature_names'], rnd_clf.feature_importances_):
    print(name, score)

```