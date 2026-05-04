import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# 1) Import pandas and read in the banklist.csv file into a dataframe called banks. 
banks=pd.read_csv("C:\\Users\\ADMIN\\Desktop\\LIBRARIES\\Numpy\\banklist.csv")
# print(banks)

# 2) Show the head of the dataframe. 
# print(banks.head())

# 3) What are the column names? 

# print(banks.columns)
 
# 4) How many States (ST) are represented in this data set? 
# print(len(banks["ST"].unique()))

 
# 5) Get a list or array of all the states in the data set. 
# print(banks["ST"].unique())
 
# 6) What are the top 5 states with the most failed banks? 
# print(banks["ST"].value_counts().head(5))
 
# 7) What are the top 5 acquiring institutions? 
# print(banks["Acquiring Institution"].value_counts().head())

# 8) How many banks has the State Bank of Texas acquired? How many of them were actually in Texas? 
# print(((banks['Acquiring Institution'] == 'State Bank of Texas') & (banks['ST'] == 'TX')).sum())

# 9) What is the most common city in California for a bank to fail in?
# print(banks[banks['ST']=='CA']['City'].value_counts().head())