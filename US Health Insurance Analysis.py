#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[7]:


df=pd.read_csv('usa_health_insurance.csv')
df


# In[9]:


df.age.mean()


# In[11]:


df.describe()


# In[27]:


df.sex.value_counts()


# In[29]:


df.sex.value_counts(normalize=True)


# In[35]:


categorical_counts = df.select_dtypes(include =['object']).apply(pd.Series.value_counts)


# In[37]:


categorical_counts


# In[39]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[45]:


plt.figure(figsize=(10,6))

numeric_data = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot= True, cmap ='coolwarm')
plt.title("Matrix")
plt.show()


# In[51]:


sns.pairplot(df, vars = ['age','bmi','charges'], hue='smoker')
plt.show()


# In[55]:


avg_charges_smokers = df.groupby('smoker')['charges'].mean()

print(avg_charges_smokers)

avg_charges_region = df.groupby('region')['charges'].mean()

print(avg_charges_region)

The venerable insurance industry is no stranger to data driven decision making. Yet in today's rapidly transforming digital landscape, Insurance is struggling to adapt and benefit from new technologies compared to other industries, even within the BFSI sphere (compared to the Banking sector for example.) Extremely complex underwriting rule-sets that are radically different in different product lines, many non-KYC environments with a lack of centralized customer information base, complex relationship with consumers in traditional risk underwriting where sometimes customer centricity runs reverse to business profit, inertia of regulatory compliance - are some of the unique challenges faced by Insurance Business.

Despite this, emergent technologies like AI and Block Chain have brought a radical change in Insurance, and Data Analytics sits at the core of this transformation. We can identify 4 key factors behind the emergence of Analytics as a crucial part of InsurTech:

Big Data: The explosion of unstructured data in the form of images, videos, text, emails, social media
AI: The recent advances in Machine Learning and Deep Learning that can enable businesses to gain insight, do predictive analytics and build cost and time - efficient innovative solutions
Real time Processing: Ability of real time information processing through various data feeds (for ex. social media, news)
Increased Computing Power: a complex ecosystem of new analytics vendors and solutions that enable carriers to combine data sources, external insights, and advanced modeling techniques in order to glean insights that were not possible before.
This dataset can be helpful in a simple yet illuminating study in understanding the risk underwriting in Health Insurance, the interplay of various attributes of the insured and see how they affect the insurance premium.

Content
This dataset contains 1338 rows of insured data, where the Insurance charges are given against the following attributes of the insured: Age, Sex, BMI, Number of Children, Smoker and Region. There are no missing or undefined values in the dataset.

Inspiration
This relatively simple dataset should be an excellent starting point for EDA, Statistical Analysis and Hypothesis testing and training Linear Regression models for predicting Insurance Premium Charges. We will start with descriptive statistics and frequency counts, then plot correlation matrix and pairplot.