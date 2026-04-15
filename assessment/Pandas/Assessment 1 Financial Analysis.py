import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\ADMIN\\Desktop\\LIBRARIES\\Pandas\\finance_economics_dataset.csv")
# print(df)
# df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
# What is the shape of the dataset?
# print("Shape:", df.shape)

# What are the column names and their data types?
# print("Data Types:", df.dtypes)

# How many unique stock indices are there?
# print("Unique Indices:", df['Stock Index'].nunique())

#What is the date range of the dataset?
# print("Date Range:", df['Date'].min(), df['Date'].max())

# Are there any missing values?
# print("Missing Values:", df.isnull().sum())

# Are there negative values in columns that should be non-negative?
# neg_values= (df.select_dtypes(include='number')<0).sum()
# print(neg_values[neg_values>0])

# What is the summary of GDP Growth (%)?
# print(" GDP Summary:", df['GDP Growth (%)'].describe())

# Are there rows with zero or near-zero trading volume?
# print("Zero Trading Volume:", (df['Trading Volume'] <= 0).sum())

#Are there any duplicate rows?
# print("Duplicate Rows:", df.duplicated().sum())

# Are there outliers in GDP, Gold, or Oil prices?
#outliers for gdp
# GDP=df["GDP Growth (%)"]
# Q1 = GDP.quantile(0.25)
# Q3 = GDP.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = GDP[(GDP < lower) | (GDP > upper)]

# print('GDP-',outliers)

#outliers for gold
# gold=df["Gold Price (USD per Ounce)"]
# Q1 = gold.quantile(0.25)
# Q3 = gold.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = gold[(gold < lower) | (gold > upper)]

# print('gold -',outliers)

#outliers for crude oil
# oil=df["Crude Oil Price (USD per Barrel)"]
# Q1 = oil.quantile(0.25)
# Q3 = oil.quantile(0.75)

# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR

# outliers = oil[(oil < lower) | (oil > upper)]

# print('oil -',outliers)

# What is the summary of Inflation Rate (%)? 
# print("Inflation Summary:", df['Inflation Rate (%)'].describe())

# What is the average unemployment rate? 
# print("Avg Unemployment:", df['Unemployment Rate (%)'].mean())

# Which index has the highest trading volume? 
# idx = df['Trading Volume'].idxmax()
# print("Index:", idx)
# print("Value:", df.loc[idx, 'Trading Volume'])

# How many stock records are from each index? 
# print("Stock Index :", df['Stock Index'].value_counts())

# What is the correlation between inflation and interest rate? 
# print("Correlation: ",df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

# What is the average Consumer Confidence Index? 
# print("Consumer Confidence:", df['Consumer Confidence Index'].mean())

# Which column has the highest standard deviation? 
# print(df.std(numeric_only=True).idxmax())

# What is the highest gold price recorded? 
# print("Highest Gold Price:", df['Gold Price (USD per Ounce)'].max())

# Which date had the highest crude oil price? 
# idx = df['Crude Oil Price (USD per Barrel)'].idxmax()
# print("Date:", df.loc[idx, 'Date'])

# What is the average corporate profit? 
# print("Avg Corporate Profit:", df['Corporate Profits (Billion USD)'].mean())

# Insightful Analysis Questions 
# # What percentage of the dataset shows negative GDP growth? 
# neg_gdp = (df['GDP Growth (%)'] < 0).sum()
# total = len(df)
# percentage_neg_gdp = (neg_gdp / total) * 100
# print("Negative GDP Growth:", round(percentage_neg_gdp, 2))

# Does high inflation correspond to higher interest rates?
# No strong relationship — interest rates are not directly moving with inflation here.
# print("Inflation vs Interest Rate : ",df['Inflation Rate (%)'].corr(df['Interest Rate (%)']))

# Is there a relationship between unemployment and consumer spending? 
# Practically no relationship in this dataset.
# print(" Unemployment vs Consumer Spending: ",df['Unemployment Rate (%)'].corr(df['Consumer Spending (Billion USD)']))

# Do higher corporate profits align with higher consumer confidence?
# print("  Corporate Profit vs Consumer Confidence: ",df['Corporate Profits (Billion USD)'].corr(df['Consumer Confidence Index'])) 

#What’s the trend of crude oil prices over time?
# x = np.arange(len(df))

# y = df['Crude Oil Price (USD per Barrel)']
# plt.plot(x, y)


# plt.title("Trend of Crude Oil Prices Over Time")
# plt.xlabel("Time")
# plt.ylabel("Crude Oil Price (USD per Barrel)")

# plt.show()

#Are gold prices inversely related to stock performance?
# Gold prices show a weak/negative relationship with stock performance
# print("Gold prices vs Close Price : ",df['Gold Price (USD per Ounce)'].corr(df['Close Price']))

# Does government debt impact consumer confidence?
# Government debt has a negative impact on consumer confidence,no 
# print("government debt vs consumer confidence : ",df['Government Debt (Billion USD)'].corr(df['Consumer Confidence Index']))

#How do mergers & acquisitions (M&A) activity correlate with stock index closing prices?
# M&A activity shows a positive correlation with stock prices
# print("mergers & acquisitions (M&A) vs stock index closing prices : ",df['Mergers & Acquisitions Deals'].corr(df['Close Price']))

#Is retail sales growth associated with GDP growth?
# not associated
# print(" retail sales vs GDP growth : ",df['Retail Sales (Billion USD)'].corr(df['GDP Growth (%)']))

#  Is stock market performance linked to consumer spending? 

# print("Stock vs Spending:",df['Close Price'].corr(df['Consumer Spending (Billion USD)']))

# Which stock index had the highest average closing price? 

# highest_index = df.groupby('Stock Index')['Close Price'].mean().idxmax()
# print("Highest Avg Closing Price:", highest_index)

# What is the relationship between interest rate and unemployment? 
# no relation
# print("Interest vs Unemployment:",df['Interest Rate (%)'].corr(df['Unemployment Rate (%)']))

# Do lower consumer confidence values coincide with higher bankruptcy rates? 
# negative co-relation
# print("Confidence vs Bankruptcy:",df['Consumer Confidence Index'].corr(df['Bankruptcy Rate (%)']))

# Which indicator has the highest correlation with stock close price? 
# corr = df.select_dtypes(include='number').corr()
# result = corr['Close Price'].drop('Close Price').abs().idxmax()
# print(result)

# Are unemployment rates lower when corporate profits are high?
# no relationship
# print("Unemployment vs Profits:",df['Unemployment Rate (%)'].corr(df['Corporate Profits (Billion USD)']))
