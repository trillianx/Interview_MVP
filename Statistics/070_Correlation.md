# Correlation

Correlation is about measuring the degree of relationship between two or more variables. These variables can have both [[Quantitative data]] or [[categorical data]]. 

## Covariance

The best way to measure whether two variables are related to each other is to measure their movement with respect to some inertial frame of reference. If both vary with respect to such a frame of reference, i.e., either in the same direction or the opposite direction, we would know that they are related. However, if one varies while the other does not, we know that they are not related. 

The inertial frame of reference is the mean of the data. The variation or the variability in the data is given by the **variance**. The variance tells us how each point in the data or for a given variable varies with its mean. We apply the same here. We measure the variation between two variables $x$ and $y$ as follows: 

$$
cov(x, y) = \sum \frac{(x_i - \bar{x})(y_i - \bar{y})}{(N-1)}
$$

This is known as **covariance**. Positive covariance indicates that both variables move in the same direction while a negative covariance suggest that they move in the opposite direction. A covariance of zero, indicates that there is no realtionship between the two variables. 

## Pearson's Correlation

When comparing two or more variables, it is always good to measure them in terms of standard units. This allows us to measure on the same scale irrespective the original scale of the variables. The best way to standardize the variables is to measure their variances in terms of standard deviations. Thus, the above equation can be rewritten as, 

$$
r = \frac{cov_{xy}}{s_xs_y} = \sum \frac{(x_i - \bar{x})(y_i - \bar{y})}{s_xs_y(N-1)}
$$

The coefficient, $r$ in the above equation si called the [[Pearson correlation coefficient]]. This correlation varies between $-1$ and $+1$. This coefficient is also used to measure the size of the effect. The table below tells us the size of the effect based on the values: 

|Values|Effect Size|
|-------|-----------|
|$\pm0.1$| Small |
|$\pm0.3$| Medium|
|$\pm0.5$| Large|

### Significance of Correlation Coefficient

While we have the coefficient value that tells us that there is an effect or there isn't. We would like to know how significant this value is. To do this, we make use of [[060_Hypothesis_Testing]]. The [[null hypothesis]] states that there is coefficient is zero while the [[alternative hypothesis]] states that it is different from zero.

To measure how significant the $r$ value is, we make use of [[z-score]]. We use z-score because we know the probability of each z-value. We can then use this probability to determine how extreme this value would be given that the null hypothesis is true. However, the problem with Pearson's $r$ is that the distribution is not normal. However, a simple transformation makes it normal: 

$$
z_r = \frac{1}{2}log_e \left (\frac{1+r}{1-r} \right)
$$

The resulting standard error is: 

$$
SE_z = \frac{1}{\sqrt{N-3}}
$$

With this, we can transform into z-scores and compute the significance:

$$
z = \frac{z_r}{SE_z}
$$

The hypothesis tes for correlation is generally perfomed using the [[t-statistic]] with $N-2$ degrees of freedom and not [[z-statistic]]. Thus, using t-statistic, we have: 

$$
t_r = \frac{r\sqrt{N-2}}{\sqrt{1-r^2}}
$$

### Confidence Intervals for $r$

The 95% confidence interval is given by, 

$$
z_r \pm(1.96 \times SE_z)
$$

We can convert this back to the $r$ values, to get confidence interval in terms of $r$: 

$$
r = \frac{e^{(2z_r)} - 1}{e^{(2z_r)} + 1}
$$

This gives us the upper and lower bounds of the coefficient. 

> Correlation say nothing about the direction of causality. It only states that two variables are related and that the effect size is quantified by the coefficient. 

The correlation between two variables is called a **bivariate correlation**. The examples of bivariate correlations are [[Pearson correlation coefficient]], [[Spearman's rho]] and [[Kendall's tau]]. **Partial correlation** looks at the relationship between two variables hwhile controlling the effect of one or more additional variables. 

### Assumptions

Pearson's correlation requires that the data are interval and the distribution is normal. The latter part is required to carry out test statistic. However, if these conditions are not satisfied, we cannot use the Pearson's test. 

### Using $R^2$ for interpretation

When we square the Person's r, we get **coefficient of determination**. This is a measure of the amount of variability in one variable that is shared by the other. 

## Spearman's rho

The [[Spearman's rho]], $r_s$ is a non-parametric statistic and is generally used when the data have violated parametric assumptions such as non-normally distributed data. The Spearman's rho works by first ranking the data and then applying Pearson's equation to those ranks. 

## Kendall's tau

The [[Kendall's tau]], $\tau$, is a non-parametric correlation. It should be used instead of Spearman's rho when you have a small data with a large number of tied ranks. This means that if you rank all of the scores and many scores have the same rank, then Kendall's tau should be used.

## Bootstrapping Correlations

Another way to deal with data that do not meet the assumptions of Pearson's $r$ is to use bootstrapping. With enough samples, we can get to the point where we can use Pearson's correlation or Spearman's tau or even Kendall's tau. 

## Comparing Correlations

