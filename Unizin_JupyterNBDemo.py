
# coding: utf-8

# In[153]:


# Remember to check working directory


# In[212]:


# Import relevant modules
import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns
from scipy import stats as st


# In[213]:


# Python variable assignment
x = 123
x


# In[214]:


# Lists are constructed using [] brackets
x = [1,2,3]
x


# In[215]:


# List comprehension to add to elements in the list
y = [x+1 for x in x]
y


# In[216]:


# Most of the time, you'll be working with more complex data structures and need more effective operations.
# Pandas is a library that provides powerful data manipulation tools
# Pandas allows for using dataframes similar to R 
# https://pandas.pydata.org/
# Read in data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
data = pd.read_csv('factor_scores.csv')
data


# In[217]:


# Can use methods to describe and look at specific examples
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
data.describe()


# In[218]:


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html
data.head(5)


# In[219]:


data.mean(axis=0)


# In[220]:


data['Motivations'].mean()


# In[221]:


data['Motivations'].min()


# In[222]:


data['Motivations'].max()


# In[223]:


# Handling Missing Data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
data.dropna(inplace=True)
data


# In[224]:


# Like R, there are a lot of way sto manipulate data
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
data.loc[data.Motivations <= 0, 'Motivations_Cat'] = 'Lo'
data.loc[data.Motivations > 0, 'Motivations_Cat'] = 'Hi'
data


# In[200]:


# Using apply method and lambda function
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
data['Visit.Frequency_Cat'] = data['Visit Frequency'].apply(lambda x: 'Lo' if x <= 0 else 'Hi')
data


# In[204]:


# Grouping data for summary
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
data.groupby(['Motivations_Cat','Visit.Frequency_Cat']).agg({'double_hashedid':'count'})


# In[205]:


# Plotting Data
# https://matplotlib.org/tutorials/introductory/pyplot.html
data.plot(kind = 'scatter',x='Motivations',y='Concentration of Effort',color='black')


# In[206]:


# There are also many graphing options for python
# Seaborn provides one option for more graphic functionality
plot = sns.regplot(x='Motivations',y='Concentration of Effort',data=data)


# In[207]:


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html
data.boxplot(column='Concentration of Effort',by='Motivations_Cat',figsize=(4,6))


# In[229]:


# Statistics 
# t-test
Motivations_Hi = data.where(data['Motivations_Cat']=='Hi').dropna()['Concentration of Effort']
Motivations_Lo = data.where(data['Motivations_Cat']=='Lo').dropna()['Concentration of Effort']
t_test = st.ttest_ind(Motivations_Lo,Motivations_Hi)
print("The t-statistic is %.3f; the p-value is %.3f"%t_test) 


# In[209]:


# Regression 
# There are a lot of libraries within Python to develop models
# statsmodels is one
import statsmodels.api as sm
import statsmodels.formula.api as smf
data.rename(columns={'Concentration of Effort':'COE'},inplace=True)
results = smf.ols('COE ~ C(Motivations_Cat)',data=data).fit()
results.summary()

