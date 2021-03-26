# Hypothesis Testing

Having looked at the data, we begin creating statistical models to explain the data. These models, as we have seen in [[050_Population_and_Samples]], allow us to go beyond the data and generalize what we observe. Much of statistics deals with creating models to fit the data at hand. 

As we have seen in other sections, the hypothesis is predictions that a theory makes. 

## Example

Let's start with an example to illustrate hypothesis testing. Suppose we have a bottle of water that states that it is 12 fl. oz. or 355 ml. We would like to know whether this is really true? We can put this problem mathematically as: 

Customer assumes that the bottle contains at least 355 ml or 

$$
\text{Quantity of Water} \geq 355 \ ml
$$
 
 while the manufacturer assumes that the bottle contains exactly 355 ml or
 
 $$
 \text{Quantity of Water} = 355 ml
 $$

Now to verify the assumption we set up the experiment. 

> There is a difference between **assumption** and **claim**. A claim is something we are unsure of and therefore needs to be tested while assumption is thought to be true which we need to reconfirm or verify. 

When formulating a statistical hypothesis, we need to ask ourselves the following questions: 

> Am I testing an assumption that already exists? 
> Am I testing a claim or assertion beyond what I already know or can know? 

Once we have formulated the questions, the next step is to create the **null** and **alternative** hypotheses.  Here are some properties of these hypotheses: 

* All statistical conclusions are made in reference to the null hypothesis
* The null and alternative hypotheses are opposite of each other. They are mutually exclusive.
* We either reject the null hypothesis or fail to reject it. This is because the null hypothesis is assumed to be true from the beginning. The whole hypothesis testing is to see whether we can reject the null hypothesis or not
* The null hypothesis can either be rejected or failed to be rejected.
	* If the null hypothesis is rejected, it gives credence to the alternative hypothesis.
	* If the null hypothesis is not rejected, we cannot confirm or deny the alternative hypothesis. Also, the lack of rejection does not mean the null hypothesis is true. It simply means the assumption remains true until we have more data to test it. 

## Null and Alternative Hypothesis

We can define null and alternative hypothesis simply as: 

> A null hypothesis is simply states that there is nothing new or different happening or that the assumption of the claim is maintained. It is given a symbol, $H_0$. 

> The alternative hypothesis states that something new or different is happening or that the assumption or the claim is challenged. It is given by the symbol, $H_a$. 

Here are some properties of null and alternative hypotheses: 

![[Pasted image 20210325155903.png]]

So, here's what happens to alternative hypothesis when the null hypothesis takes the following property: 

|Null Hypothesis Property|Aternative Hypothesis Property|
|--------------------------|--------------------------------|
|$H_0 =$|$H_a \neq$|
|$H_0 \leq$|$H_a >$|
|$H_0 \geq$|$H_a <$|

Coming back to our example, we have the following: $H_0 = 355$ ml while $H_1 \neq 355$ ml. Now if we test 50 bottles picked randomly and measure the volume and find that the mean volume is 355 ml, we fail to reject the null hypothesis. However, if the data indicates that they were not 355 ml, we reject the null hypothesis and state that our assumptions  were not held under the analysis. We have statistical support for alternative hypothesis. 

