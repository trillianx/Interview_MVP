# Test Statistic

The basic idea behind much of statistics is to create models that can explain the observations. The models that fit the data better allow us to make better hypotheses (predictions) and go beyond the data and generalize our theory. 

The simple way to determine whether our model fits the data well (our hypothesis is a good explanation of the data) is to compare variations between systematic and unsystematic errors. This tells us how good the model is at explaining the data against how bad it is: 

![[Pasted image 20210323104628.png]]

The ratio of systematic to unsystematic variance or effect to error is called a **test statistic**.  We will see shortly that there are a lot of test statistic such as the [[t-statistic]], [[F-test]], and the [[$\chi^2$ test]]. The exact form of the test statistic depends on which test statistic we are talking about. But in a crude sense, all test statistic represent the same: the ratio of variance explained by the model we've fitted to the data and the variance that cannot be explained by the model. If the variance explained by the model is large, the model is considered a good fit to the data. In this case the test statistic will be large. If not, the test statistic will be small. 

Now the test statistic is a statistic that has known properties, specifically we know how frequently different values of this statistic occur. There is a distribution associated with these statistic values, just like we have frequency distribution. Each statistic value, therefore, has a probability associated with it. This allows us to determine how likely it would be that we would obtain a particular value of the test statistic if there were no effect (i.e. the null hypothesis were true). In general, if the statistic gets bigger, the probability of them occurring becomes smaller. When this probability falls below 0.05 (Fisher's Criterion), we accept this as given us enough confidence to assume the test statistic, as large as this, could not have happened if there were no effect (i.e., we reject the null hypothesis). This gives us confidence that the alternative hypothesis is true. The test statistic is said to be **significant**. 

## [[Shapiro-Wilk Test]]

Shapiro-Wilk test is a test for normality of data. It compares the scores in the sample to a normally distributed set of scores with the same mean and standard deviation. If the test is not significant, ($p > 0.05$) then the distribution is said to be normal while if the test is significant ($p < 0.05$), then the distribution is said to be non-normal. 

The weakness of the Shapiro-Wlik test is that with large samples, small deviation from normal will show up as significant, which will result in non-normal distribution. Therefore, this test should be used in conjunction with [[Q-Q plot]] and by simply plotting the sampling distribution. 

## [[Levene's Test]]

