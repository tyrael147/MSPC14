# %% Import required libraries
import polars as pl
import matplotlib.pyplot as plt
import numpy as np

# %% Load the dataset
df = pl.read_csv('data/dataset.csv').with_columns(
    pl.col('Date').cast(pl.Date)
)
df = df.drop_nulls()
df.shape

# %% Basic Line Plot - Sales over time
plt.figure(figsize=(12, 6))
sales_by_date = df.group_by('Date').agg(pl.col('Total Amount').sum())
plt.plot(sales_by_date['Date'], sales_by_date['Total Amount'])
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Bar Chart - Sales by Product Category
plt.figure(figsize=(10, 6))
sales_by_category = df.group_by('Product Category').agg(pl.col('Total Amount').sum()).sort('Total Amount', descending=True)
plt.bar(sales_by_category['Product Category'], sales_by_category['Total Amount'])
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Pie Chart - Sales Distribution by Gender
plt.figure(figsize=(8, 8))
sales_by_gender = df.group_by('Gender').agg(pl.col('Total Amount').sum())
plt.pie(sales_by_gender['Total Amount'], labels=sales_by_gender['Gender'], autopct='%1.1f%%')
plt.title('Sales Distribution by Gender')
plt.tight_layout()
plt.show()

# %% Scatter Plot - Age vs Total Amount
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Total Amount'], alpha=0.5)
plt.title('Relationship between Age and Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.tight_layout()
plt.show()

# %% Histogram - Age Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, edgecolor='black')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# %% Box Plot - Price Distribution by Product Category
plt.figure(figsize=(12, 6))
# Create a list of data for each product category
data = [df.filter(pl.col('Product Category') == category)['Price per Unit'].to_numpy() 
        for category in df['Product Category'].unique()]
plt.boxplot(data, tick_labels=df['Product Category'].unique())
plt.title('Price Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Price per Unit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Multiple Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: Average Transaction Amount by Gender
avg_by_gender = df.group_by('Gender').agg(pl.col('Total Amount').mean()).sort('Gender')
ax1.bar(avg_by_gender['Gender'], avg_by_gender['Total Amount'])
ax1.set_title('Average Transaction Amount by Gender')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Average Amount')

# Subplot 2: Transaction Count by Product Category
category_counts = df.group_by('Product Category').count().sort('count', descending=True)
ax2.bar(category_counts['Product Category'], category_counts['count'])
ax2.set_title('Number of Transactions by Product Category')
ax2.set_xlabel('Product Category')
ax2.set_ylabel('Number of Transactions')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

