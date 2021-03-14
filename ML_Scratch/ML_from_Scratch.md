

# Machine Learning From Scratch

My notes include writing well-known ML algorithms from scratch. These are often asked in coding interviews. I will start by first defining the algorithm. Then go into the steps of the algorithm and finally write a code to run the algorithm. The code has been taken from the following YouTube videos: 

*   [Python Engineer](https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA)
*   

## kNN 

**Definition**

The kNN algorithm is used in classification problems. The kNN algorithm does not learn from the data instead it uses a distance metric, often Eucliedian Distance, to determine whether an observation belongs to a certain group or not. 

**Algorithm Steps**

The kNN algorithms follows these steps: 

1.  Measure distances from the new point's position to all other points in the dataset. use the L2-norm
2.  Sort the distances increasing order
3.  Take the top k points
4.  Take the mode of their labels
5.  Assign the label to the new point

For $n$ dimensions, the Euclidean distance is given by: 
$$
d = \sqrt{\sum_{i=1}^n (q_i - p_i)^2}
$$
where $(q_i, p_i)$ are the pair positions of a point. When $n= 2$, we would have: 
$$
d = \sqrt{(q_1 - p_1)^2 + (q_2-p_2)^2}
$$
**Algorithm**

```python
import numpy as np


class KNN():
    def __init__(self, k=3):
        self.k = k
        
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)
        
    def _predict(self, x):
        # Compute Euclidean Distance
        distances = 
        # get k nearest samples
        
        # majority vote
        
```

