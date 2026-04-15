import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\ADMIN\\Desktop\\LIBRARIES\\Pandas\\Retail Data.csv")
# print(df)

# 1. View the structure of the dataset (columns, types, missing values). 
# print(df.info())
# print("Missing Values:", df.isnull().sum())

# 2. What is the shape (rows, columns) of the dataset? 
# print("Shape:", df.shape)

# 3. Are there any duplicate records?
# print("Duplicate Records:", df.duplicated().sum())

# 4.  Are there any missing or corrupted entries in Ship Date, Order Date, or numeric columns?
# print("Missing in Date Columns:", df[['Ship Date', 'Order Date']].isnull().sum())

# 5.  Convert Order Date and Ship Date to datetime. 
df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'],dayfirst=True)

# 6.  Check for future or inconsistent shipping dates.
# print("Invalid Shipping Dates:", (df['Ship Date'] < df['Order Date']).sum())

# 7.  Convert price columns to numeric (remove $ and commas). 
price_cols = ['Cost Price', 'Retail Price', 'Profit Margin',
              'Sub Total', 'Discount %', 'Discount $',
              'Order Total', 'Shipping Cost', 'Total']

for col in price_cols:
    df[col] = df[col].str.replace('$', '') 
    df[col] = df[col].str.replace(',', '') 
    df[col] = df[col].str.replace('%', '')   
    
    df[col] = pd.to_numeric(df[col])

# 8. What are the unique values in Customer Type and Order Priority? 
# print("Customer Type:", df['Customer Type'].unique())
# print("Order Priority:", df['Order Priority'].unique())

# 9. What are the most common shipping modes? 
# print("Shipping Mode:", df['Ship Mode'].value_counts())

# 10. Which cities have the highest number of orders? 
# print("Top Cities:", df['City'].value_counts())

# 11. What’s the range of order quantities and prices? 
# print("Range of order quantities: ","Min:", df['Order Quantity'].min(), "Max:", df['Order Quantity'].max())
# print("Range of cost price : ","Min:", df['Cost Price'].min(), "Max:", df['Cost Price'].max())

# 12. Create a new column for shipping duration. 
# df['Shipping Duration'] = (df['Ship Date'] - df['Order Date']).dt.days

# print(df[['Order Date', 'Ship Date', 'Shipping Duration']].head())

# 13. Are there any orders with zero or negative total or quantity? 
# invalid_values = df[(df['Order Quantity'] <= 0) | (df['Total'] <= 0)]
# print("Invalid Quantity/Total:", invalid_values.shape[0])


# 14. Are all discount percentages matching discount dollar amounts?
# df['Expected Discount $'] = (df['Sub Total'] * df['Discount %']) / 100

# discount_mismatch = df[abs(df['Expected Discount $'] - df['Discount $']) > 1]
# print("Discount Mismatches:", len(discount_mismatch))

#15.Check for mismatches in total calculation.
# df['Calculated Total'] = df['Sub Total'] - df['Discount $'] + df['Shipping Cost']
# total_mismatch = df[abs(df['Total'] - df['Calculated Total']) > 1]
# print("\nTotal Mismatch:", len(total_mismatch))

# 16.  Identify top 5 products by order quantity.
# print("Top Products:", df.groupby('Product Name')['Order Quantity'].sum().sort_values(ascending=False).head())

# 17. Which Account Manager handled the most revenue? 
# print("\nTop Manager:\n", df.groupby('Account Manager')['Total'].sum().sort_values(ascending=False).head())

# 18.  What is the average shipping cost by mode? 
# print("Avg Shipping:", df.groupby('Ship Mode')['Shipping Cost'].mean())

# 19. Find the most profitable product. 
# df['Profit'] = df['Sub Total'] - (df['Cost Price'] * df['Order Quantity'])
# print("\nTop Profit Products:\n", df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head())




# Insightful Analysis Questions 
# 1. What is the total revenue generated across all orders? 
# print("Total Revenue:", df['Total'].sum())

# 2. Which customer type generates more revenue? 
# print("Revenue by Customer Type:", df.groupby('Customer Type')['Total'].sum().sort_values(ascending=False).head(1))

# 3.  How does order priority affect revenue? 
# print("Revenue by Order Priority:", df.groupby('Order Priority')['Total'].sum())

# 4. What is the average profit margin by product category? 
# print("Avg Profit Margin by Category:", df.groupby('Product Category')['Profit Margin'].mean())

# 5. What is the most profitable product overall? 
df['Profit'] = df['Sub Total'] - (df['Cost Price'] * df['Order Quantity'])
# print("Most Profitable Product:",df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(1))

# 6. How many days does it usually take to ship an order? 
df['shipping days'] = (df['Ship Date']-df['Order Date']).dt.days
# print(df['shipping days'].mean())

# 7. Do longer shipping times impact profit margins? 
# negative correlation suggests longer shipping may reduce profitability. yes
# print("Correlation (Shipping Duration vs Profit):", df['shipping days'].corr(df['Profit']))

# 8. Which city brings in the highest revenue? 
# print("8. Top City:",df.groupby('City')['Total'].sum().sort_values(ascending=False).head(1))

# 9. Which account manager generated the most revenue? 
# print("\nTop Manager:\n", df.groupby('Account Manager')['Total'].sum().sort_values(ascending=False).head(1))

# 10.  Which shipping mode is most cost-effective (lowest avg. shipping)? 
# print("Avg Shipping Cost:",df.groupby('Ship Mode')['Shipping Cost'].mean().sort_values().head(1))

# 11.  Do higher discounts reduce profits? 
# Higher discounts generally reduce profit margins.
# print(" Correlation (Discount vs Profit):",df['Discount %'].corr(df['Profit']))

# 12. Which state has the highest number of orders? 
# print("Top State:",df['State'].value_counts().head(1))

# 13. What is the average discount % across all orders?
# print("Avg Discount %:", df['Discount %'].mean()) 

# 14. What is the average total spend per order? 
# print("\n14. Avg Order Spend:", df['Total'].mean())

# 15.Are certain containers (e.g., Small Box, Wrap Bag) more profitable? 
# small box
# print("Profit by Container:",df.groupby('Product Container')['Profit'].mean().sort_values(ascending=False))