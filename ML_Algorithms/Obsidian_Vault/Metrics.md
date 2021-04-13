# Metrics
In this section, we look at various metrics that are used to evaluate the performance of a machine learning algorithm. These metrics differ by the type of the problem, that is whether the problem is [[regression]] or [[classification]]. 

## Classification

We begin by listing the metrics used for classification problems. 

### Confustion Metrix

The [[confusion matrix]] is used for a binary class or multi-class problem. It is easier to explain for a binary classes. For binary classes, the confusion matrix simply a $2\times2$ matrix. It looks like this: 

![[Pasted image 20210412094010.png]]

The confusion matrix is created on all the predictions that a classifier has made. There are four categories into which the observations can go: 

* **True Positive (TP)** - These are observations that are labeled as positive and predicted to be positive.

* **False Positive (FP)** - These are observations that are labeled as negative but are predicted to be positive.

* **True Negative (TN)** - These are observations that are labeled as negative and predicted to be negative

* **False Negative (FN)** - These observation are labeled as positive but are predicted to be negative. 

> False Positive as True Negative while False Negative are True Positive

The confusion matrix in scikit-learn is created in the following way: 

```python
from sklearn.metrics import confusion_matrix
confusion_matrix(y, y_pred)
```

While the confusion matrix gives us the overall picture on how the algorithm is doing, we can summarize the confusion matrix using other classification matrix. 

* **Accuracy** - We define [[accuracy]] as the ratio of observations that have been correctly identified as belonging to the positive and negative classes over all the observations. 

* **Precision**- We define [[precision]] as the ratio of observations that are true positive and all observations belonging to the positive classes (i.e. TP and FP). We write this as: 

$$
\text{precision} = \frac{TP}{TP + FP}
$$

* **Recall** - We define [[recall]] as the ratio of observations that are predicted correctly as true positive and all observations that are truly positive (i.e. TP and FN). We write this as: 

$$
\text{recall} = \frac{TP}{TP + FN}
$$

* **F1-score** - The [[F1-score]] is the harmonic mean of precision and recall. F1-score is particularly useful to compare two or more classifiers. The difference between mean and harmonic mean is that the latter gives more weight to low values. As a result, the classifier will only get a high F1-score if both recall and precision are high.

$$
F_1\text{ score} = 2 \times \frac{precision \times recall}{precision + recall}
$$

* **True Positive Rate (TPR)** - The [[true positive rate]] tells us how many of the observations that are labeled as positive were correctly predicted to be positive. This is **recall**. It is also known as [[sensitivity]]. The TPR gives us the probability of correctly detecting an event of interest.

$$
\text{True Positive Rate} = \frac{TP}{P} = \frac{TP}{TP + FN}
$$
* **False Positive Rate (FPR)** - This gives us the probability of **false alarm** or making a [[Type I error]], which is falsely identifying an event as something that is not. 
$$
\text{False Positive Rate} = \frac{FP}{N} = \frac{FP}{FP + TN}
$$

* **True Negative Rate** - The [[true negative rate]], also known as [[specificity]]. This is the probability of correctly tagging an event as not the event of interest.

$$
\text{True Negative Rate} = \frac{TN}{N} =\frac{TP}{TP + FN}
$$

* **False Negative Rate** - The [[false negative rate]] is probability of **missed event** of interest. This gives us the probability of making a [[Type II error]].

$$
\text{False Negative Rate} = \frac{FN}{P} =\frac{FN}{FN + TP}
$$

We can compute precision and recall in scikit-learn as follows: 

```python
from sklearn.metrics import precision_score, recall_score, f1_score

print("Precision: ", np.round(precision_score(y_train, y_train_pred),2))
print("Recall: ", np.round(recall_score(y_train, y_train_pred),2))
print("F1-score: ", np.round(f1_score(y_train, y_train_pred),2))
```

### Creation of Classification Metrics

The classification metrics are based on the positive and negative metrics. These originate from the decision boundary that is set by the algorithm. Generally, the decision boundary used by a classifier is at 50%. Here is an example of a decision boundary for an Iris dataset: 

![[Pasted image 20210412102450.png]]

Observations greater than the decision boundary belong to one class while observations less than the decision boundary belong to the other class. In the figure suppose, the RHS is the positive class and LHS is the negative class. We see that there are two blue observations that should belong to the negative class but belong to the positive class. These are **false positives**. Similarly, we have green observations that should belong to the positive class but are predicted to belong to the negative class. These are **false negatives**. 

### Precision-Recall Trade-off

Let's move the decision boundary to the right so all the negative observations (blue icons) are correctly classified as belonging to the negative class. If we do that we have $FP = 0$, so our **precision = 1**. But we see that we have a lot of false negatives (green icons). So, our **recall** has decreased. Now if we move the decision boundary to the left such that all green observations are correctly classified. We have $FN = 0$, so our **recall = 1**. But we have a lot of blue observations in the positive class that should be negative, false positive. This is known as precision-recall trade-off. 

The **[[precision-recall curve]]** is constructed by moving the decision boundary all the way from one class to the other class. Each time the decision boundary is moved, the precision and recall is calculated and stored. The result is then plotted in a figure as a function of decision boundary (threshold): 

![[Pasted image 20210412104232.png]]

In scikit-learn we can create the above figure as follows: 

```python
# Get precision and recall values for all thresholds
from sklearn.metrics import precision_recall_curve
precisions, recalls, thresholds = precision_recall_curve(y_train, y_train_pred)

# Plot to view the curves
plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
plt.legend()
plt.ylabel('Score')
plt.xlabel('Threshold')
```

### ROC Curve

The [[ROC curve]] allows us to evalute multiple binary classifiers. We do this by plotting the TPR and FPR of the classifiers. The closer the curves are to the top left corner the better is the performance of a classifier. 

![[Pasted image 20210412104716.png]]

Here is how we can do that in scikit-learn:

```python
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_train, y_train_pred)

plt.plot(fpr, tpr, linewidth=2)
plt.plot([0,1],[0,1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
```

### AUC
The [[AUC]] is simply the area under the ROC curve.

```python
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(y_train, y_train_pred)
print(np.round(auc_score, 2))
```

>*   Use the Precision Recall Curve whenever the positive class is rare or when you care more about the FP than the FN.
>*   Use the ROC curve otherwise