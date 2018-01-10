
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write up, download this file as a PDF or HTML file and submit in the next section.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# Independent variable is a variable that stands alone and isn't changed by the other variables you are trying to measure. Dependent variable is something that depends on other factors.
# 
# The different conditions between each experiment are independable variable. It is controlled by the tester, the same for all the participant and have direct influence in the time taken to perform the task, 
# Time in Congruent words' condition and incongruent word conditions are dependable variable which depends on the test condition, and the participants' physical and mental condition.  

# (2) What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

# Null Hypothesis (H0: μ1 = μ2) : There is no significant difference in the population average amount of time it takes to state the colors of the words in a congruent(μ1) or incongruent condition(μ2).
# 
# Alternative Hypothesis (H1: μ1 != μ2): There is significant difference in the population average amount of time it takes to state the colors of the words in a congruent(μ1) or incongruent condition(μ2).

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[49]:


#Import the library used in the following analysis 
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[50]:


df = pd.read_csv('stroopdata.csv')
df.head()


# In[51]:


#Create descrptive summary for stroop dataset*/
df.describe()


# Mean is one measure of central tendency. The average number for Congruent column is 14.0511 while the average number for Incongruent column is 22.0159. Therefore, the average time in incongruent condition is longer than average congruent condition.
# 
# Range is measure of variability. the min number and max number for Congruent column is (8.6300,22.3280).
# the min number and max number for Incongruent column is (15.6870,35.2550). The Incongruent time has larger range than congruent time.

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[52]:


#The distribution for congruent condition time
plt.hist(df['Congruent'],bins=np.arange(min(df['Congruent']), max(df['Congruent']) + 2, 2))
plt.title('Graph 1: The Histogram for Congruent Group Time')
plt.xlabel('Congruent Group Time')
plt.legend()
plt.show()


# In[53]:


#The distribution for incongruent condition time
plt.hist(df['Incongruent'], color ='orange',bins=np.arange(min(df['Incongruent']), max(df['Incongruent']) + 2, 2))
plt.title('Graph 2: The Histogram for Incongruent Group time')
plt.xlabel('Incongruent Group Time')
plt.legend()
plt.show()


# From graph 2, we can see that the bin between 20 and 22 has 6 observation, which is highest frequency in Incongruent Group time.
# also, there are 2 outliers around time 35.0 since there is a break in histogram. 
# 
# Furthermore, from graph 1 and 2, we can tell that the average Incongruent Group time is longer than congruent Group time.  

# (5) Now, perform the statistical test and report the results. What is the confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# I will use a two sample two-tailed dependent t-test (also called the paired t-test or paired-samples t-test) for this analysis,the reason are as following: 
# Firstly,t-test is used in samples from the population to try to make inferences about the population, which fits the purpose of this hypothesis test scenario; Secondly, as Incongruent and Congruent columns are dependable variables, we should use dependent t-test or paried t-test. Additionally,since the sample size for this dataset is 24, which is small sample and  the variances of two normal distributions are unknown, T-test is commonly used with small sample sizes, for testing the difference between the samples.
# 
# We conduct a paired t-test to see whether this difference is significant at a 95% confidence level.

# In[54]:


#Use a two sample two-tailed t-test for this analysis.
t, p = stats.ttest_rel(df['Incongruent'],df['Congruent'],axis=0)


# In[55]:


#Given p and t values from a two-tailed test.
(t, p)


# As p-value 4.1030-08 is smaller than 0.05, we reject the null hypothesis test that (H0: μ1 = μ2), therefore, I am 95% confident that the time the participant takes in the congruent words condition is different from the participant takes in the incongruent words condition. This is different from what i expect.

# In[56]:


df['difference'] =  df['Incongruent'] -df['Congruent']


# In[28]:


df['difference'].describe()


# In[29]:


d_bar = df['difference'].mean()
print("mean difference:", d_bar)
std = df['difference'].std()
print("standard deviation of the differences: ", std)


# In[57]:


from math import *

SE_d_bar = df['difference'].std()/(sqrt(24))
print("standard error of the differences: ", SE_d_bar)


# In[58]:


t_statistic = df['difference'].mean()/SE_d_bar
                       
print("t-statistic: ", t_statistic)


# In[59]:


#degree of freedom  = n-1 =23
df = 23
#Calculate T critical value 
print(stats.t.ppf(1-0.025, df))


# Since the t-statistic is less than t critical value -2.06865 or greater than 2.06865, we are 95% condifident that we can reject the null hypothesis. 
