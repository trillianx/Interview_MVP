# Population & Sampling

In the previous sections we saw how we start with an idea or an observation, create a theory, make hypotheses, collect data to validate our theory and solidy it. What we generally do through this process is create models of the phenomenon of interest. These are known as **statistical models**. We build statistical models because we can make predictions and draw inferences about the real-world phenomenon. The better the fit of these models to real-world phenomenon, the more accurate they would be in their predictions and inferences. 

As a researcher, we are interested in finding results that apply to an entire population of people or things. A [[population]] is any complete collection of observations or potential observations that exist around us. So, a population can be large like the population of a country or the world, sometimes it can be small like the number of women in a concert. When the population is too large it is impossible to collect all the observations from it. Therefore, in order to better understand the population, we create a model of the population by collecting a small subset of data from the population. We then use the behavior within the sample to inter things about the behavior in the population. The samples from the population are collected at random. This is known as random sampling.  A random sampling is a process in which each sample from the population has an equal probability of being picked. 

There are two types of statistics: the [[030_Descriptive Statistics]] provides tools to describe, summarize, and organize variability in the observations while [[inferential statistics]] uses  samples from the population and generalizes the properties of the population from the limited set of samples. 

This chapter focuses on the single most important concept in [[inferential statistics]]--the concept of sampling distribution. A sampling distribution serves as a frame of reference for every outcome, among all possible outcomes that could occur just by chance. 

## Mean as a Model

The simplest model that we can build is the [[Mean]]. For every possible value of a given variable, our model has just the same value, the average of all possible values of the given variable. We can access the quality of our model by computing the **sum of squares**. The sum of squares is defined as: 

$$
\text{sum of squares} = \sum_{i=1}^N (x_i - \mu)^2
$$

This would be the total error between the model and the observations. The weakness of sum of squares is that it increases with increasing $N$. So, we divide it by the total number of observations. As we will see shortly this is defined as [[Variance]]. 

> Larger the variance, the poor the fit. Smaller the variance, excellent the fit! 

It is interesting to note that the "goodness of fit" is computed by measuring the squared deviations. The squared deviations is defined by, 

$$
\text{deviations} = \sum (observed - model)^2
$$

This is nothing but the sum of squares. However, this idea will come time and time again.

## What is Sampling Distribution?

It is often hard to work with [[population]] as it can be impossible given the size or can be prohibitively expensive. Instead, we rely on the samples from the population. However, a single sample may not give us the true picture of the population as it may or may not represent the true population. Therefore, we rely on taking multiple sets of samples from the population. Hundreds of these sets are more likely to be representative of the population. 

The process is to take the sets of samples from the population, compute their mean and construct a distribution of sample means. Such a distribution is called [[sample distribution of sample means]] or simply sample distribution. 

> The sampling distribution of the mean refers to the [[probability distribution]] of means for all possible random samples of a given size from some population

By creating a sampling distribution of sample means we, effectively, **create a model of the population**. This becomes our framework. Next time when we take a sample from the population, we can compare it with our framework to decide whether the sample is representative of the population or not. 

So, if we have a mean of the sample distribution of the sample means is 500 and and standard deviation of 2.3, and suppose we draw a sample from the population and get a value of 533 for a given sample, we can tell how representative this sample of 533 is. We would find that it is quite rare. We will see this come into play when we work with [[hypothesis testing]]. 

## Shape of the Sample Distribution

>The [[central limit theorem]] states that, regardless of the shape of the population, the shape of the sampling distribution of the sample mean approximates a normal curve if the sample size is sufficiently large

This is a very powerful theorem. Basically, it states that it does not matter what the shape of the population is. If we take sufficient number of samples, the shape of the sampling distribution of sample means will always be a [[021_Normal Distribution]]. This is actually really great because we know a whole lot about normal distribution. So, once we have enough samples, we can determine the mean and standard deviation of our sampling distribution and we can effectively know everything about the population. 

The central limit works because in a normal curve, the intermediate values are the most prevalent and extreme values, either large or smaller, occupy the tapered flanks. When the sample size is large, it is _most likely_ that any single sample will contain the full spectrum of small, intermediate, and large scores from the parent population, whatever its shape.

## Mean and Standard Deviation

The [[Mean]] of a sampling distribution, $\mu_{\bar{X}}$ of the sample means **always** equals the mean of the population, $\mu$. The mean of the sampling distribution is written as:
$$
\mu_{\bar{X}} = \mu
$$

The [[standard deviation]] of the sampling distribution of the sample means equals the **standard deviation of the population** divided by the **square root of the [[sample size]]**. The standard deviation of the sampling distribution of the sample means is called a [[standard error]]. It is written as: 

$$
\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}}
$$

We will see later what happens when we cannot find the population standard deviation.

Now the variance depends on whether we are looking at the variance in the [[population]] distribution or [[sample]] distribution. 

The **variance in a population distribution** is given by:

$$\sigma^2 = \frac{\sum(X - \mu)^2}{N}$$

where N is the total population. 

The **variance in a sample distribution** is given by, 

$$s^2 = \frac{\sum (X - \mu_\bar{X})^2}{n - 1}$$

where $n$ is the number of samples. We used $n-1$ in the denominator of the sample variance calculations. This is due to the **degrees of freedom**. 

> The degrees of freedom (df) refers to the number of values that are free to vary, given one or more mathematical restrictions, in a sample being used to _estimate_ a population characteristic.

## Effect of Sample Size
It is interesting to note that when we have large sample size, the variability in the sampling distribution is much smaller than the variability in the population. This is because the variability in the population is due to individual observations while the variability in the sample distribution is due to the means of samples. Therefore, the standard error is statistically more stable than the population standard deviation, thanks to the [[effect of sample size]]. 

The table below keeps track of the symbols associated with means and standard deviations: 

![[Pasted image 20210318143918.png]]

