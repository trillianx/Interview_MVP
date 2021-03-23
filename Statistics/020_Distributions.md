# Distributions

In sections [[011_Data Types]] and [[012_Surveys_Experiments]] we learned about what to measure and how to measure. Once we have collected all of the data, we are ready to analyse it. However, before we begin the analysis process, it is important to size the terrain we are dealing with. This is sort of exploratory data analysis. 

The data we collect can be pretty large. So, in order to understand we try to create metrics that allow us to summarize the data. One way to summarize the data is through the creation of distributions. These distributions can be tables or graphs. Let's see some types of distributions. 

* [[Frequency Distribution]] - is a list of observations and count of the times they appear in the data. Sometimes we take frequency distribution of a single observation or create buckets of observations and count the frequency of observations that fall into buckets. This is known as frequency distribution of grouped data. 
* [[Relative Frequency Distribution]] - Rather than taking the raw counts of observations, we take the percentage of observations that appear in the data. This is done by first counting the number of times each observation appears. Then, dividing each count of the observation by the total number of obsrevations. In other words, a relative frequency distribution is the normalized frequency distribution. The sum of the relative frequency distribution over all observations equals 1. 
* [[Proportion Frequency Distribution]] - is basically multiplying each value in the relative frequency by 100. This results in a whole number. 
* [[Cumulative Frequency Distribution]] - is taking the cumulative sum of the proportion frequency distribution. 
* [[Percentile Ranks]] - allows us to determine the position of an observation relative to other observations. A percentile rank of an observation is simply the cumulative score of that observation in cumulative frequency distribution. 

So far the tools we have seen create tables. However, we can also visualize these frequency distributions. The visualization is primarily done using histograms. Histograms are used to plot [[Quantitative data]].  Histogram simply plot the counts of observations in each bin. In other words, plot the frequency distribution table we created above into a graph. Other non-common type is the stem and leaf display. 

When a histogram of the frequency distribution is created, we can see the shape of the distribution. When a distribution is composed of discrete variable it is called a [[discrete distribution]] while when a distribution has continuous variable, it is called a [[continuous distribution]]. 

Here are some common distributions:

* A [[021_Normal Distribution]] is a symmetric distribution that has just one peak. It is a bell-shaped distribution.
* A [[bimodal distribution]] is a distribution that has two peaks. A multi-modal distribution is a distribution that has multiple peaks. 
* A [[skewed distribution]] is a distribution that is lop-sided. A positively skewed distribution is a distribution that has a long tail in the direction of positive values while a negatively skewed distribution is a distribution that has a long tail in the direction of negative values. 
