#!/usr/bin/env python
# coding: utf-8

# # Unemployment Analysis of India (2019-20)

# ### Importing all the necessary libaries/modules.

# In[1]:


# Importing all the required modules in the beginning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px


# ### Reading data from (.csv)

# In[2]:


# Raeding the given excel file
excelFile = pd.read_excel("Unemployment in India.xlsx")

# Converting the excel file to (.csv) file and saving it in the local drive
excelFile.to_csv ("Unemployment in India.csv", index = None, header=True)

# Raeding that csv file and converting it into Pandas DataFrame for simplicity
data = pd.DataFrame(pd.read_csv("Unemployment in India.csv"))


# In[3]:


# Printing top 5 rows of the dataset
data.head()


# In[4]:


# Printing the basic informations of the dataset
data.info


# In[5]:


data.describe


# ### Pre-processing the dataset

# In[6]:


# Checking if the dataset contain any missing values or not
print(data.isnull().sum())


# ###### The output explains the dataset contain 14 missing values in each columns. So, we need to remove them before moving any further.

# In[7]:


# Dropping/removing all the rows which contain NaN (Null Values) in the dataset
data = data.dropna()


# In[8]:


# Again checking if the dataset contain any missing values or not
print(data.isnull().sum())


# ###### Now the output explains the dataset doesn't contain any missing values anymore, as it shows every column in the dataset has zero null values.

# In[9]:


# We will rename all the columns stored in dataframe for our better understanding
data.columns = ["States", "Date", "Frequency", "Estimated Unemployment Rate", "Estimated Employed", 
                "Estimated Labour Participation Rate", "Area"]

# Printing the modified dataframe/dataset
data


# ### Analyzing the Dataset

# #### Correlation

# In[10]:


# Code to finding the correlation b/w the columns/features (columns only with numeric/logical values) of the dataset
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(14,12))
sb.heatmap(data[["Estimated Unemployment Rate", "Estimated Employed", "Estimated Labour Participation Rate"]].corr())
plt.title("Correlation b/w the features of the dataset")
plt.savefig("2019_20 Correlation.png")
plt.show()


# #### Plotting Employment & Unemployment Rate Graph

# In[11]:


# Estimated number of employees according to different regions of India
plt.figure(figsize=(10,10))
plt.title("Indian Employment Rate based on different areas")
sb.histplot(x = "Estimated Employed", hue = "Area", data = data)
plt.savefig("2019_20 Indian Employment Rate based on different areas.png")
plt.show()


# In[12]:


# Estimated number of unemployed according to different regions of India
plt.figure(figsize=(10,10))
plt.title("Indian Unemployment Rate based on different areas")
sb.histplot(x = "Estimated Unemployment Rate", hue = "Area", data = data)
plt.savefig("2019_20 Indian Unemployment Rate based on different areas.png")
plt.show()


# #### Plotting Unemployment rate graph compared to different states of India

# In[13]:


# Unemployed figures with respect to the Area plotting inside a single graph
unep = data[["Area", "Estimated Unemployment Rate"]]
figure = px.sunburst(unep, path = ["Area"],
                     values = "Estimated Unemployment Rate",
                     width = 700, height = 700, color_continuous_scale = "RdYlGn",
                     title = "Unemployment Rate in India compared with each Area.")
figure.show()


# # END
