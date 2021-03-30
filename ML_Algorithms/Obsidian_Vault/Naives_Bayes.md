
# Naive Bayes
The Naive Bayes is a [[supervised]] learning algorithm used for binary and multinomal [[classification]] algorithm that is based on [[Bayes Theorem]]. It classifies a given example based on the prior probability of the class, and the probability of the feature in the context. 

## How does it work? 
The Naive Bayes algorithm is used in the classification. To understand how it works consider an example of spam filtering. We have a training set of emails that are labeled as `spam` and `not spam`. Here are the steps it will follow: 
1. The Naive Bayes algorithm then computes the probability of these two classes or labels, the **prior probabilities**. This would be `P(spam)` and `P(not spam)`
2. It will find all the unique words that exist within the training set irrespective of the labels, and their frequency. 
3. It computes the probabilities of each word, in the context of the two groups. For example, it would could count the frequency of a word 'refund' in the `not spam` group and divide it by the total number of words in the `not spam` and record this as `P('refund'|not spam)` and it will do the same in the group `spam` and compute 	`P('refund'|spam)`. 
4. When it encounters a new phrase, say 'get refund', it will compute the probabilities in the following way for spam: 
$$
P(\text{get refund}|\text{spam}) = P(\text{spam})\times P(\text{get}|\text{spam}) \times P(\text{refund}|\text{spam})
$$

5. It will then repeat this for `not spam`. 
6. It then compares the probabilities between groups and reports the label with the highest probabilities.

The reason it is called *Naive Bayes* is because it looks at each independently rather than an interaction between terms. For example, the probability of `get refund` is the same as `refund get`. In other words, the order of the words does not matter. This is generally not the case in a language. 

> If a word does not exist in one of the classes, it can lead to an overall probability of zero. Therefore, a constant value (usually `1`) is added to each word count so the probabilities are non-zero. 

## Machine Learning Mathematics

In Naive Bayes, we are interested in assigning a class to an observation that is not in our training. Consider this to be our hypothesis, $h$. Thus, we are interested in computing the probability of hypothesis given data, $d$, which we can write as: $P(h|d)$. From Bayes theorem, we have: 
$$
P(h|d) = \frac{P(d|h)\times P(h)}{P(d)}
$$

* $P(h|d)$ is called the **poterior probability**, which is something we are interested to compute. 
* $P(d|h)$ is the probability of data given the hypothesis is true.
* $P(h)$ is the probability of hypothesis being true (regardless of the data). This is known as the **prior probability**.
* $P(d)$ is the probability of data (regardless of the hypothesis)

After counting the probabilities for various hypothesis, for example `spam` and `not spam` are two hypotheses, we select a hypothesis with the highest probability. This is the maximum probable hypothesis and is formally called the **maximum a posterior (MAP) hypothesis**. It is written as 

$$
\text{MAP(h)} = max(P(h|d))
$$

The $P(d)$ is a normalizing term which we can drop when calculating the most probable hypothesis as it is a constant. 

## What is the Cost Function? 

Naive Bayes does not have a cost function. It simply computes the probabilities from the training set and assigns the probability to the example based on the probabilities it has computed. 

## What are the Hyperparameters? 

There are no hyperparameters in Naive Bayes. 

## What are the Strengths and Weaknesses? 

**Strengths**
* Fast to train and make predictions
* Provide probabilities directly
* Easy to interpret

**Weaknesses**
* It assumes conditional independence. In other words, as we say the order of the words does not matter. So, the interaction of words or features are not take into consideration. 

## Where is Naive Bayes used? 
It is mostly used when:
* the conditional independence is not important
* The categories are well-separated and the model complexity is less important
* For vey high dimensionality data, when model complexity is less important

# Gaussian Naive Bayes
The version of Naive Bayes that is applied in practice is the [[Gaussian Naive Bayes]]. The Gaussian Naive Bayes makes an assumption that the data in each category is described by a Gaussian distribution with no covariance between dimensions. This model can be fit by simply finding the mean and standard deviation of the points within each label. The figure shows two categories with their Gaussian distributions: 

![[Pasted image 20210329142525.png]]

[Source](https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html)

The smaller concentric circles are constant probabilities that are larger. The probabilities decrease as we go out radially. For a given example, we can compute the probability that it belongs to each of the classes and output class that corresponds to the maximum probability. 

## Naive Bayes in Scikit-Learn
In scikit-learn, we make use of Gaussian Naives Bayes instead: 

```python
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))

```