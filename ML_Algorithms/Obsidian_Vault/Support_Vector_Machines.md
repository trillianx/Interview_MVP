## Support Vector Machines

Support Vector Machine (SVM) is used for both linear and non-linear [[regression]] and [[classification]] problems. SVM is also used for outlier detection. 

## How Does it Work? 
The SVM algorithms works in sort of the same way for regression and classification settings. Let's look at the similarity and differences of both. 

### Classification

In the classification setting, we will look at two cases: when the data can be linearly separable and when it is non-linearly separable.

#### Linear SVC

In the classification settings, SVM tries to find a region wide enough that separates the classes. This region can be linear or non-linear. To find such a region, the SVM employs **margins**. These are lines that separate the classes. Consider two classes. In this case, the one margin is closer to one class while the other is closer to the second class. Half-way between the two margins is the main margin or the **decision function**. The two margins are constructed by finding observations of each classes that allow to keep the two classes separate. These are called **support vectors**. The margins pass through these support vectors. Notice that adding more observations on either side of the classes will not change the margins. 

![[Pasted image 20210412084416.png]]

When instances of one class are closer to the main margin or on the opposite side of the main margin, it is called a **violation**. A classifier that does not allow any violation to occur is called a **hard-margin classifier**. In reality, such classifiers don't work. Intead, we use a **soft-margin classifier** which allows certain number of violations to take place. The number of allowed violations are set by a hyperparameter, $C$.

The linear SVC makes prediction of a given observation $\bf{x}$ by simply computing the decision function: $\bf{w^Tx} + b$. If the result is positive, the prediction class is positive class (1) else, it is a negative class (0): 

![[Pasted image 20210412085850.png]]

#### Non-linear SVC

When the underlying data is non-linear, we make use of non-linear SVM. The main thing in non-linear SVM is the use of kernel. This is known as the **kernel trick**. 


## What are the Hyperparameters?

## What are the Strengths & Weaknesses? 

## Where is SVM used? 

## SVM in Scikit-Learn

