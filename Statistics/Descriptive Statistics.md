# Descriptive Statistics
In general, [[Descriptive Statistics]] provides us with tools to describe the data. 

The main tools that are used to describe the data are the following: 

* [[Mode]] - is the most frequently occuring score. When a distribution is multi-modal, the mode will be more than a single score. The mode is used for [[categorical data]]. 

* [[Mean]] - is defined as the sum of all the scores divided by the total number of scores. 

* [[population]] mean - The mean definition above is that of population mean. The equation below gives us the population mean. 


$$\mu = \frac{\sum_{i=1}^N x_i}{N}$$

* [[samples]] mean - is defined as summing all the scores of the samples and dividing it by the total number of samples. 

$$\bar{X} = \frac{\sum_{i=1}^N x_i}{n}$$

> The mean serves as a balance point for its frequency distribution. This is because when you sum all the deviations from the mean, they add up to zero. 

* [[Median]] - reflects the middle value when observations are sorted in increasing order. The median is more robust to outliers than the mean. The median is also used for [[Ordinal data]]. 

## Describing Variability
The tools listed above tell us the **central tendency** of the data, i.e, where is the center of the data distribution. However, it does not tell us how wide or narrow the distribution is. The width of the distribution is given by the **measure of variabilty**. 

Variability is important because large variability within observations translates into **less statistical stability** while small variability within observations translates to **more statistical stability**. 

The tools used to measure variability are as follow: 

[[Range]] - is the difference between the largest and the smallest scores in the distribution. As range depends on two scores, it fails to correctly summarize the distribution. Also, the range is highly sensitive to outliers. 

[[IQR]] - is the interquartile range. It is simply the range of the middle 50% of the scores. In other words, it is the distance between the 25th and 75th percentile. 

## Variance

[[Variance]] - is defined as the mean of the squared deviations from the mean. The sum of squared deviation scores are sometimes written as the **sum of squared errors**. 

$$\text{variance} = \frac{\text{sum of squared deviation scores}}{\text{number of scores}}$$

> Rather than using the squared deviations, we can also use the sum of absolute values of deviations. This is known as **Mean Absolute Deviation** or MAD. 

Now the variance is depends on whether we are looking at the variance in the [[population]] distribution or [[sample]] distribution. 

The **variance in a population distribution** is given by:

$$\sigma^2 = \frac{\sum(X - \mu)^2}{N}$$

where N is the total population. 

The **variance in a sample distribution** is given by, 

$$s^2 = \frac{\sum (X - \bar{X})^2}{n - 1}$$

We used $n-1$ in the denominator of the sample variance calculations. This is due to the **degrees of freedom**. 

> The degrees of freedom (df) refers to the number of values that are free to vary, given one or more mathematical restrictions, in a sample being used to _estimate_ a population characteristic.

The only weakness in variance is that the value is squared. In other words, if a variable is say weight, the variance will return the squared weights. 

## Standard Deviation
The [[standard deviation]] gets rid of the squared term in the variance by taking the square root of the variance. Therefore, the standard deviation returns the units in the format we desire: 

$$\text{standard deviation} = \sqrt{\text{variance}}$$

> You might find it helpful to think of the standard deviation as a _rough_ measure of the average (or standard) amount by which scores deviate on either side of their mean

The standard deviation tells us how far a score lies from the mean. So, we can use it to tell us where the majority of scores line within a given frequency distribution. 

> For most frequency distributions, a majority (often as many as 68%) of all scores are within one standard deviation on either side of the mean. 

The standard error can also tell us how far from the mean the most extreme scores lie.

> For most frequency distributions, a small minority (often as small as 5%) of all scores deviate more than two standard deviations on either side of the mean. 

The [[normal distribution]] is ideal frequency distribution as it has been studied extensively. As we will see later, it is a distribution that occurs very often in nature. The standard deviation in a normal distribution tells us a lot about where the scores lie: 

* 68% of the scores lie within 1 standard deviation
* 95% of the scores lie within 2 standard deviations
* 99% of the scores lie within 3 standard deviations

Knowing this will become very important when we do [[hypothesis testing]]. 

In summary, we can say that: 

> The **mean** is a measure of **position**

> The **standard deviation** is a measure of **distance** (on either side of the mean)

## Variability of Qualitative and Ranked Data
The measure of variability for [[Qualitative data]] does not exist. This is because it does not make sense. However, for [[Ordinal data]] data we can determine the variability by identifying extreme scores or ranks. 