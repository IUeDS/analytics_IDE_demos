
# coding: utf-8

# In[1]:


# Remember to check working directory


# In[44]:


# Import relevant modules
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns
from scipy import stats as st
# Set printing display option for non-exponential format
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[45]:


# Python variable assignment
x = 123
x


# In[46]:


# Unassigning a variable
x = None 
x


# In[47]:


# Lists are constructed using [] brackets
x = [1,2,3]
x


# In[48]:


# List comprehension to add to elements in the list
y = [x+1 for x in x]
y


# In[49]:


# Most of the time, you'll be working with more complex data structures and need more effective operations.
# Pandas is a library that provides powerful data manipulation tools
# Pandas allows for using dataframes similar to R 
# https://pandas.pydata.org/
# Read in data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
data = pd.read_csv('factor_scores.csv')
data


# In[50]:


# Can use methods to describe and look at specific examples
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
data.describe()


# In[51]:


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
data.head(5)


# In[52]:


data.mean(axis=0)


# In[53]:


data['Motivations'].mean()


# In[54]:


data['Motivations'].min()


# In[55]:


data['Motivations'].max()


# In[56]:


# There are multiple ways to get to a specific observation
data.loc[data['double_hashedid']=="QYd/Tw04aPsBQuaQV8nK3w=="]


# In[57]:


# Handling Missing Data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
data.dropna(inplace=True)
data


# In[58]:


# Like R, there are a lot of way sto manipulate data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
data.loc[data.Motivations <= 0, 'Motivations_Cat'] = 'Lo'
data.loc[data.Motivations > 0, 'Motivations_Cat'] = 'Hi'
data


# In[59]:


# Using apply method and lambda function
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
data['Visit_Frequency_Cat'] = data['Visit Frequency'].apply(lambda x: 'Lo' if x <= 0 else 'Hi')
data


# In[60]:


# Grouping data for summary
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
data.groupby(['Motivations_Cat','Visit_Frequency_Cat']).agg({'double_hashedid':'count'})


# In[61]:


# Plotting Data
# https://matplotlib.org/tutorials/introductory/pyplot.html
data.plot(kind = 'scatter',x='Motivations',y='Concentration of Effort',color='black')


# In[62]:


# There are also many graphing options for python
# Seaborn provides one option for more graphic functionality
plot = sns.regplot(x='Motivations',y='Concentration of Effort',data=data)


# In[63]:


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
data.boxplot(column='Concentration of Effort',by='Motivations_Cat',figsize=(4,6))


# In[64]:


# Statistics 
# t-test
Motivations_Hi = data.where(data['Motivations_Cat']=='Hi').dropna()['Concentration of Effort']
Motivations_Lo = data.where(data['Motivations_Cat']=='Lo').dropna()['Concentration of Effort']
t_test = st.ttest_ind(Motivations_Lo,Motivations_Hi)
print("The t-statistic is %.3f; the p-value is %.3f"%t_test) 


# In[65]:


# Regression 
# There are a lot of libraries within Python to develop models
# statsmodels is one
import statsmodels.api as sm
import statsmodels.formula.api as smf
data.rename(columns={'Concentration of Effort':'COE'},inplace=True)
results = smf.ols('COE ~ Motivations',data=data).fit()
results.summary()

