# Boosting

Boosting is a technique that is used for both [[classification]] and [[regression]] problems. Boosting creates a series of weak learners where each weak learner learns from the mistakes of the previous weak learner. Thus, boosting is a sequential learning technique. 

## How Does it Work?

Boosting works in the following way: 

1. A subset of training data is created using bootstrap.  
2. Each observation is given the same weight.
3. A weak learner is given the weighted dataset.
4. A weak learner is trained on this dataset. 
5. The observations that the learner gets wrong are given higher weights
6. The number of observations a model got wrong is registered
7. We repeat steps 2-5.
8. We stop when we have exhausted all of the weak learners.
9. Give weights to the models based on the number of errors each model made. Higher weights go to models with lower errors.
10. The final prediction is made using the weighted average of all the predictions. 
11. We use another subset of training data using bootstrap and repeat steps 1-10. 

Graphically, this process looks like the following: 

![[Pasted image 20210330095724.png]]

We see that each weak learner gets part of the data correctly none of all of the data. However, when combined, the boosting technique is able to correctly classify a complex pattern. In other words, the performance of the overall model is sequentially boosted. 

The table below shows the differences between using a single algorithm, [[Bagging]] and boosting. 

| Type       | Single                | Bagging                         | Boosting                          |
| ---------- | --------------------- | ------------------------------- | --------------------------------- |
| Dataset    | Uses complete dataset | Bootstrap                       | Weighted bootstrap                |
| Training   | One iteration         | Multiple iteration but parallel | Multiple iteration but sequential |
| Prediction | Single estimate       | Arithmetic mean                 | Weighted average                  |
| Process    | Train and keep model  | Train and keep models           | Train and weigh models            |

Let's look at some boosting algorithms














