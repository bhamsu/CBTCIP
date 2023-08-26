#!/usr/bin/env python
# coding: utf-8

# # Unemployment Analysis of India (2020)

# ### Importing all the necessary libaries/modules.

# In[1]:


# Importing all the required modules in the beginning
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
import plotly.io as pio


# ### Reading data from (.csv)

# In[2]:


# Raeding the given excel file
excelFile = pd.read_excel("Unemployment_Rate_upto_11_2020.xlsx")

# Converting the excel file to (.csv) file and saving it in the local drive
excelFile.to_csv ("Unemployment_Rate_upto_11_2020.csv", index = None, header=True)

# Raeding that csv file and converting it into Pandas DataFrame for simplicity
data = pd.DataFrame(pd.read_csv("Unemployment_Rate_upto_11_2020.csv"))


# In[36]:


# Printing top 5 rows of the dataset
data.head()


# In[3]:


# Printing the basic informations of the dataset
data.info


# In[4]:


data.describe


# ### Pre-processing the dataset

# In[5]:


# Checking if the dataset contain any missing values or not
print(data.isnull().sum())


# ###### The output explains the dataset doesn't contain any missing values, as it shows every column in the dataset has zero null values.

# In[6]:


# We will rename all the columns stored in dataframe for our better understanding
data.columns = ["States", "Date", "Frequency", "Estimated Unemployment Rate", "Estimated Employed", 
                "Estimated Labour Participation Rate", "Region", "Longitude", "Latitude"]

# Printing the modified dataframe/dataset
data


# ### Analyzing the Dataset

# ##### Correlation

# In[7]:


# Code to finding the correlation b/w the columns/features (columns only with numeric/logical values) of the dataset
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(10,10))
sb.heatmap(data[["Estimated Unemployment Rate", "Estimated Employed", "Estimated Labour Participation Rate", 
                 "Longitude", "Latitude"]].corr())
plt.title("Correlation b/w the features of the dataset")
plt.savefig("2020 Correlation.png")
plt.show()


# ##### Plotting Employment & Unemployment Rate Graph

# In[8]:


# Estimated number of employees according to different regions of India
plt.figure(figsize=(10,10))
plt.title("Indian Employment Rate based on different Regions")
sb.histplot(x = "Estimated Employed", hue = "Region", data = data)
plt.savefig("2020 Indian Employment Rate based on different Regions.png")
plt.show()


# In[9]:


# Estimated number of unemployed according to different regions of India
plt.figure(figsize=(10,10))
plt.title("Indian Unemployment Rate based on different Regions")
sb.histplot(x = "Estimated Unemployment Rate", hue = "Region", data = data)
plt.savefig("2020 Indian Uneployment Rate based on different Regions.png")
plt.show()


# ##### Plotting Unemployment rate graph compared to different states of India

# In[10]:


# Unemployed figures with respect to the Region & State plotting inside a single graph
unep = data[["States", "Region", "Estimated Unemployment Rate"]]
figure = px.sunburst(unep, path = ["Region", "States"],
                     values = "Estimated Unemployment Rate",
                     width = 700, height = 700, color_continuous_scale = "RdYlGn",
                     title = "Unemployment Rate in India compared with each Region & State.")

figure.show()


# # END
