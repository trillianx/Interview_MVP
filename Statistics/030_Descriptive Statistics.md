# Descriptive Statistics

Once we have the data, we can create [[Frequency Distribution]] to get a sense of what sort of data we have. We can use histogram to plot the frequency distribution and see its shape. So, the distribution of our data helps us define the shape. 

As we will see here, the frequency distribution can be completely defined by two parameters: the mean and the standard deviation. The mean gives the center of the frequency distribution while the standard deviation gives the width. 

## The Center

The center of a frequency distribution, also known as the **central tendency** is given by: 

* [[Mean]] - is defined as the sum of all the scores divided by the total number of scores. 

> The mean serves as a balance point for its frequency distribution. This is because when you sum all the deviations from the mean, they add up to zero. 

* [[Median]] - reflects the middle value when observations are sorted in increasing order. The median is more robust to outliers than the mean. The median is also used for [[Ordinal data]]. 

* [[Mode]] - is the most frequently occuring score. When a distribution is multi-modal, the mode will be more than a single score. The mode is used for [[categorical data]]. 

## Describing Variability
The tools listed above tell us the **central tendency** of the data, i.e, where is the center of the data distribution. However, it does not tell us how wide or narrow the distribution is. The width of the distribution is given by the **measurement of variabilty**. 

Variability is important because large variability within observations translates into **less statistical stability** while small variability within observations translates to **more statistical stability**. 

The tools used to measure variability are as follow: 

[[Range]] - is the difference between the largest and the smallest scores in the distribution. As range depends on two scores, it fails to correctly summarize the distribution. Also, the range is highly sensitive to outliers. 

[[IQR]] - is the interquartile range. It is simply the range of the middle 50% of the scores. In other words, it is the distance between the 25th and 75th percentile. 

## Variance

[[Variance]] - is defined as the mean of the squared deviations from the mean. The sum of squared deviation scores are sometimes written as the **sum of squared errors**. Therefore, the variance is average error between the mean and the observations. 

$$\text{variance} = \frac{\text{sum of squared deviation scores}}{\text{number of scores}}$$

> Rather than using the squared deviations, we can also use the sum of absolute values of deviations. This is known as **Mean Absolute Deviation** or MAD. 

The only weakness in variance is that the value is squared. In other words, if a variable is say weight, the variance will return the squared weights. 

## Standard Deviation
The [[standard deviation]] gets rid of the squared term in the variance by taking the square root of the variance. Therefore, the standard deviation returns the units in the format we desire: 

$$\text{standard deviation} = \sqrt{\text{variance}}$$

> You might find it helpful to think of the standard deviation as a _rough_ measure of the average (or standard) amount by which scores deviate on either side of their mean

The standard deviation tells us how far a score lies from the mean. So, we can use it to tell us where the majority of scores line within a given frequency distribution. 

> For most frequency distributions, a majority (often as many as 68%) of all scores are within one standard deviation on either side of the mean. 

The standard error can also tell us how far from the mean the most extreme scores lie. 

## Populations & Samples

The means and the standard deviations of [[050_Population and Samples]] are equally important. As we will see in the populations and samples, we can infer the population mean from the sample mean and standard deviation of the population from the sample standard deviation. The sample standard deviation is called the [[standard error]]. 

> For most frequency distributions, a small minority (often as small as 5%) of all scores deviate more than two standard deviations on either side of the mean. 

> The **mean** is a measure of **position**

> The **standard deviation** is a measure of **distance** (on either side of the mean)

## Variability of Qualitative and Ranked Data
The measure of variability for [[013_Qualitative data]] does not exist. This is because it does not make sense. However, for [[Ordinal data]] data we can determine the variability by identifying extreme scores or ranks. 