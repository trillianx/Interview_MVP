# Normal Distribution

Normal distribution is one of the most important [[020_Distributions]] in statisitcs. This is because it is a distribution that is extremely well studied. It is used extensively in [[inferential statistics]] as we will see later. For any given normal distribution, if we know the [[Mean]] and the [[standard deviation]], we can use a standard normal table and get the properties of the distribution. 

Let's look at some properties on a normal distribution. 

* The total area under the curve is 1
* A normal distribution is a theoretical curve defined by a continuous variable
* The lower half of the normal curve is the mirror image of its upper half
* The peak of the normal distribution is at the center, or the midway of the distribution
* The mean, mode, and the median coincide and are located at the midway point. 
* The standard deviation of the normal distribution controls the width. Smaller standard deviation correspond to normal distributions that have narrow width while large standard deviation corresponds to a wider distribution. 

## Standard Deviation

The standard deviation in a normal distribution tells us a lot about where the scores lie: 

* 68% of the scores lie within 1 standard deviation
* 95% of the scores lie within 2 standard deviations
* 99% of the scores lie within 3 standard deviations


## Standard Normal Curve
A [[standard normal curve]] is a normal curve with a mean of 0 and standard deviation of 1. 

If a curve is approximately normal, it can be converted to a standard normal curve through the conversion of z-scores. In other words, take the mean and the standard deviation of a curve. Compute the [[z-score]] for all of its scores. The resultant distribution is a standard normal curve. 

The advantage of a standard normal curve is that to find the probability of a given score or proportion between two scores, we can use the standard normal table to get the answer. 

## [[Assumptions]]

The statistical models we create as based on assumptions. When these assumptions are broken, we cannot draw conclusions from these models. Different models assume different things and if we are going to use these models, we need to ensure that their assumptions are respected. 

A parameter is statisics refers to an aspect of the population while a statistic refers to the aspect of the population. For example, the population mean is a parameter while a sample mean is a statistic. A parametric test makes an assumption about the population parameters and the distributions that the data came from. Nonparametric tests on the other hand, do not assume anything about the population parameters. Generally, every parametric test has an associated non-parametric test. 

The assumptions of parametric tests are: 

* **Normally Distributed Data** - Most parametric tests assume that the distribution is a normal distribution. 
* **Homogeneity of Variance** - This assumption means that the variance should be the same throughout the data. This truly means that the data or samples at hand has come from the same population. In correlational design, this means that the variance of one variable should be stable at all levels of the other variable.
* **Interval Data** - Data should be measured at least at the interval level. 
* **Independence** - This assumption changes based on the test you are using. For example, in the independent design, this means that one participant does not influence the other. In the repeated-design the scores are not independent as they are influenced by what was done earlier. However, the behavior of one participant is independent of the other or is not influenced.

### Assumption of Normality

The assumption of normality does not mean that the data should be normal. This is because in most cases we do not have access to the population to know for sure. However, what the normality means is that the sampling distribution of sample means, the **sampling distribution**, should be normally distributed. If the sample distribution is normal, the sampling distribution will also be normal. From the central limit theorem, we also know that if the samples are large, irrespective of the shape of the population, the sampling distribution will be normal.

The normality of a distribution can be checked in the following ways: 

* **Visually** - We can visually plot the data
	* We can visually do that by simply plotting the distribution and see if it looks normal. This is not quite adequate but a quick way of determining the normality of the distribution. 
	* The use of **[[Q-Q plot]]**, which is a quantile-quantile plot. The Q-Q plots the cumulative values we have in our data against the cumulative probability of a particular distribution. In this case that would be the normal distribution. So, effectively the Q-Q plot compares distribution of our data with a theoretical distribution. If both distributions are same or similar, the Q-Q plot will be a 1:1 line. Any deviation from it will indicate to us that the distribution is not normal. 
* **Using Numbers**
	* We can use the [[Shapiro-Wilk Test]] to determine whether a distribution is normal or not. 

### Homogeneity of Variance

The homogeneity of variance means that as you go through levels of one variable, the variance of the other should not change. For example, consider the ringing in the ears after a concert. The concert happens at various cities. So, the cities are our levels for the given variable concert. The homegeneity of variance states that the variance in the measurement of ringing as measured across cities should be approximately the same. If the variance among measurements differ from city to city (i.e. between levels of a variable), then we have a case of heterogeneity of variance. See example below: 

![[Pasted image 20210323135907.png]]

[[Levene's Test]] measures whether the variance among levels or different groups are equal. If the Levene's test is significant ($p \leq 0.05$) then we conclude that the variances are significantly different and therefore our assumption of homogeneity of variances has been violated. However, if Leven's test is not signficant, ($p > 0.05$) then the variances are roughly equal and the assumption is tenable. 

The weakness of Levene's test is that with large sample sizes, small differences in group variances can produce a Levene's test that is signficant. A useful double check is to use [[Hartley's F]] - also known as the **variance ratio**. This is the ratio of variances between the group with the biggest variance and the group with the smallest variance. 

## Correcting Problems in the Data

### Outliers

One of the common problems in data are the **outliers**. Outliers can have large impact on the model that is used to fit the data. Therefore, it is important to remove the outliers before fitting a model to the data. 

Outliers can be identified using the [[IQR]]. Typically, if a value is $k$ times below the 25th percentile or above the 75th percentile, then it tagged as an outlier. Typically, $k=1.5$. Extreme outliers are for $k=3$. 

Another way to detect an outlier is to convert the distribution into [[z-score]]. We know that values that are more than $3-\sigma$ have a very low probability and therefore can be tagged as outliers. 

### Non-normal Distribution

Transforming the data is important and is generally used to correct for the distributional problem and/or unequal variances including outliers. However, one needs to be careful when doing transformations. 

> Transforming the data does not change the relationship between variables but change the differences between different variables. 

So, if you are looking at relationships between variables (e.g. regression analysis), you are fine to transform the data. However, if you are looking at how the variable changes over time, then a simple transformation won't help. You will need to transform all the levels of those variables. 

The table shows some common data transformations: 

|Data Transformation|Explanation|Can Correct for|
|---------------------|------------|----------------|
|Log Transformation ($log(X_i$)|Removes the positive skew. If your data contain zero or negative values add a constant so the values positive|Positive skew; unequal variance|
|Square root transformation ($\sqrt{X_i}$)|Brings the large scores closer to the center|Positive skew; unequal variance|
|Reciprocal Transformation ($1/X_i$)|Reduces impact of large scores. Use instead $(1/X_{highest}-X_i$) to ensure that small scores don't become too high.|Positive skew; unequal variance
|Reverse Score Transformations|Subtract each score from the highest score. Make sure to transform back|Negative skew|

There are many transformations that exist. The best transformation to use comes from trial and error. 

### When transformation don't work

Not everyone agrees that transforming the data is a good idea. Here's what a transforming the data can do: 

1. Tranforming the data can change the hypothesis being tested. If we are comparing two means of two distributions and transform these distributions using log transformation, we are not testing geometric means rather than arithmetic means.
2. Transformations can also change the construct we are measuring. When we transform, we may end up measuring a construct we really did not want to measure. 
3. Wrong transformation can result in a conclusion that is worse than not having transformed the data. 
4. Transformation of the data can be limited to small samples as large samples, over 30, are typically normally distributed as the central limit theorem tells us. 
5. Sometimes a statistical model can still work on non-normal data. When the assumptions are violated but the model is still accurate, the model is said to be **robust** and the test to be a **robust test**. An example of a robust test is the [[F-test]] in [[ANOVA]]. The F-test performs well both in cases when the distribution is normal and when it is skewed.

In conclusion, it is important to think about data transformation before doing one. 

There are some robusts tests that one can perform instead of transformations. These are: 

1. **Trimmed Mean**: Here the researcher decides the amount of data from the extremities to be removed before the computation of the mean. This could be 5% or 10% or more. 
2. **M-estimator**: This is exactly the same as trimmed mean but rather having the user input the amount to be trimmed, the M-estimator decides this empirically. 
3. **Bootstrap** - This method is used particularly when we have small sample size. Bootstrap treats the sample distribution as population distribution and takes hundreds of small samples from the sample distribution. The sample distribution of sample means would then be a normal distribution. The mean and standard error of this distribution can then help infer the properties of the original small sample distribution. 