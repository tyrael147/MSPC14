# %% Import required libraries
import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# %% Set the style to resemble scientific journals like Nature
# Set the style to a clean, minimal look
sns.set_style("whitegrid")
sns.set_context("paper", font_scale=1.2)

# Create a custom color palette inspired by Nature's color scheme
nature_colors = ["#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F", "#8491B4", "#91D1C2", "#DC0000", "#7E6148", "#B09C85"]
sns.set_palette(nature_colors)

# Custom figure style
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
plt.rcParams['axes.linewidth'] = 1.2
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['xtick.major.width'] = 1.2
plt.rcParams['ytick.major.width'] = 1.2
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlepad'] = 15

# %% Load the dataset
df = pl.read_csv('data/dataset.csv').with_columns(
    pl.col('Date').cast(pl.Date)
)
df = df.drop_nulls()

# %% Basic Line Plot - Sales over time
plt.figure(figsize=(12, 6))
sales_by_date = df.group_by('Date').agg(pl.col('Total Amount').sum()).sort('Date')
sns.lineplot(x=sales_by_date['Date'], 
             y=sales_by_date['Total Amount'], 
             linewidth=2, color=nature_colors[0])
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
from datetime import datetime
plt.figure(figsize=(12, 6))
sales_by_date = df.group_by('Date').agg(pl.col('Total Amount').sum()).sort('Date').filter(
        pl.col("Date").is_between(datetime(2023, 3, 1), datetime(2023, 7, 1)),
)
sns.lineplot(data=sales_by_date,
                x='Date', 
                y='Total Amount', 
             linewidth=2, color=nature_colors[0]) # what if we assign a color for each category?
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
from datetime import datetime
plt.figure(figsize=(12, 6))
sales_by_date = df.group_by(['Date','Product Category']).agg(pl.col('Total Amount').sum()).sort('Date').filter(
        pl.col("Date").is_between(datetime(2023, 3, 1), datetime(2023, 7, 1)),
)
sns.lineplot(data=sales_by_date,
                x='Date', 
                y='Total Amount', 
             linewidth=2, hue='Product Category') 
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Bar Chart - Sales by Product Category
plt.figure(figsize=(10, 6))
sales_by_category = df.group_by('Product Category').agg(pl.col('Total Amount').sum()).sort('Total Amount', descending=True)
sns.barplot(x=sales_by_category['Product Category'], 
            y=sales_by_category['Total Amount'], 
            palette=nature_colors,
           hue=sales_by_category['Product Category'])
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Pie Chart - Sales Distribution by Gender
# Seaborn has no piechart by default
plt.figure(figsize=(8, 8))
sales_by_gender = df.group_by('Gender').agg(pl.col('Total Amount').sum())
plt.pie(sales_by_gender['Total Amount'], labels=sales_by_gender['Gender'], autopct='%1.1f%%', 
        colors=nature_colors[:2], wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title('Sales Distribution by Gender')
plt.tight_layout()
plt.show()

# %% Scatter Plot - Age vs Total Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Age'], y=df['Total Amount'], alpha=0.6, color=nature_colors[0], s=80)
plt.title('Relationship between Age and Purchase Amount')
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.tight_layout()
plt.show()

# %% Histogram - Age Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, color=nature_colors[1], edgecolor='black', linewidth=1.2)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# %% Box Plot - Price Distribution by Product Category
plt.figure(figsize=(12, 6))
sns.boxplot(x='Product Category', y='Price per Unit', data=df.to_pandas(), 
            palette=nature_colors, hue='Product Category')
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
sns.barplot(x=avg_by_gender['Gender'], 
            y=avg_by_gender['Total Amount'], 
            palette=nature_colors[:2], hue=avg_by_gender['Gender'],ax=ax1)
ax1.set_title('Average Transaction Amount by Gender')
ax1.set_xlabel('Gender')
ax1.set_ylabel('Average Amount')

# Subplot 2: Transaction Count by Product Category
category_counts = df.group_by('Product Category').count().sort('count', descending=True)
sns.barplot(x=category_counts['Product Category'], 
            y=category_counts['count'], 
            palette=nature_colors, hue=category_counts['Product Category'],ax=ax2)
ax2.set_title('Number of Transactions by Product Category')
ax2.set_xlabel('Product Category')
ax2.set_ylabel('Number of Transactions')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

# %% Heatmap - Correlation Matrix
plt.figure(figsize=(10, 8))
# Select numeric columns
numeric_df = df.select(['Age', 'Quantity', 'Price per Unit', 'Total Amount'])
# Calculate correlation matrix
correlation_matrix = numeric_df.corr()
# Convert to pandas for seaborn
corr_pandas = correlation_matrix.to_pandas()
# Create heatmap
sns.heatmap(corr_pandas, annot=True, cmap='RdBu_r', center=0, 
            square=True, linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.title('Correlation Matrix of Numeric Variables')
plt.tight_layout()
plt.show()

# %% Violin Plot - Price Distribution by Product Category
plt.figure(figsize=(12, 6))
sns.violinplot(x='Product Category', y='Price per Unit', data=df, 
               palette=nature_colors,hue='Product Category')
plt.title('Price Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Price per Unit')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %% Faceted Plot - Age Distribution by Gender and Product Category
plt.figure(figsize=(14, 8))
# Convert to pandas for faceted plot

g = sns.FacetGrid(df, row='Gender', col='Product Category', height=2, aspect=1.5)
g.map_dataframe(sns.histplot, x='Age', bins=10, color=nature_colors[0])
g.set_axis_labels('Age', 'Count')
g.fig.suptitle('Age Distribution by Gender and Product Category', y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# %% Regression Plot - Age vs Total Amount with Confidence Interval
plt.figure(figsize=(10, 6))
sns.regplot(x='Age', y='Total Amount', data=df, 
            scatter_kws={'alpha': 0.5, 'color': nature_colors[0]},
            line_kws={'color': nature_colors[1], 'linewidth': 2},
            ci=95)
plt.title('Relationship between Age and Purchase Amount with Regression Line')
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.tight_layout()
plt.show()

# %% Custom Publication-Ready Figure
# Create a multi-panel figure with a layout similar to scientific publications
fig = plt.figure(figsize=(15, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Panel A: Sales by Product Category
ax1 = fig.add_subplot(gs[0, 0])
sales_by_category = df.group_by('Product Category').agg(pl.col('Total Amount').sum()).sort('Total Amount', descending=True)
sns.barplot(x=sales_by_category['Product Category'], 
            y=sales_by_category['Total Amount'], 
            palette=nature_colors,
            hue=sales_by_category['Product Category'],
            ax=ax1)
ax1.set_title('A. Total Sales by Product Category')
ax1.set_xlabel('Product Category')
ax1.set_ylabel('Total Sales Amount')
ax1.tick_params(axis='x', rotation=45)

# Panel B: Age Distribution
ax2 = fig.add_subplot(gs[0, 1])
sns.histplot(df['Age'], bins=20, color=nature_colors[1],
             edgecolor='black', linewidth=1.2, ax=ax2)
ax2.set_title('B. Age Distribution of Customers')
ax2.set_xlabel('Age')
ax2.set_ylabel('Frequency')

# Panel C: Correlation Heatmap
ax3 = fig.add_subplot(gs[1, 0])
numeric_df = df.select(['Age', 'Quantity', 'Price per Unit', 'Total Amount'])
correlation_matrix = numeric_df.corr()
corr_pandas = correlation_matrix.to_pandas()
sns.heatmap(corr_pandas, annot=True, cmap='RdBu_r', 
            center=0, square=True, linewidths=0.5, cbar_kws={'shrink': 0.8}, ax=ax3)
ax3.set_title('C. Correlation Matrix of Numeric Variables')

# Panel D: Box Plot
ax4 = fig.add_subplot(gs[1, 1])
sns.boxplot(x='Product Category', 
            y='Price per Unit', data=df.to_pandas(), 
            palette=nature_colors,
            hue='Product Category',
            ax=ax4)
ax4.set_title('D. Price Distribution by Product Category')
ax4.set_xlabel('Product Category')
ax4.set_ylabel('Price per Unit')
ax4.tick_params(axis='x', rotation=45)

# Panel E: Scatter Plot with Regression
ax5 = fig.add_subplot(gs[2, 0])
sns.regplot(x='Age', y='Total Amount', data=df, 
            scatter_kws={'alpha': 0.5, 'color': nature_colors[0]},
            line_kws={'color': nature_colors[1], 'linewidth': 2},
            ci=95, ax=ax5)
ax5.set_title('E. Age vs Purchase Amount with Regression Line')
ax5.set_xlabel('Age')
ax5.set_ylabel('Total Amount')

plt.tight_layout()
plt.show()

# %%
