# %% [markdown]
# # Data Manipulation with Polars
# This notebook demonstrates various data manipulation techniques using Polars, including joins, aggregations, date/time operations, string operations, and data export.

# %% [markdown]
# ## Imports and Setup

# %% [markdown]
#

# %%
import polars as pl
from pathlib import Path
import datetime

# Define the data directory path
DATA_DIR = Path("data")

# %% [markdown]
# ## 1. Creating Sample DataFrames for Join Examples

# %%
# Create sample dataframes for join examples
employees_df = pl.DataFrame({
    "employee_id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "department_id": [101, 102, 101, 103, 102]
})

departments_df = pl.DataFrame({
    "department_id": [101, 102, 103, 104],
    "department_name": ["HR", "IT", "Finance", "Marketing"],
    "location": ["New York", "San Francisco", "Chicago", "Boston"]
})

print("Employees DataFrame:")
print(employees_df)
print("\nDepartments DataFrame:")
print(departments_df)

# %% [markdown]
# ## 2. Join Operations

# %% [markdown]
# ### Inner Join
# An inner join returns only the rows where there is a match in both dataframes.

# %%
# Inner join example
inner_join_df = employees_df.join(
    departments_df,
    left_on="department_id",
    right_on="department_id",
    how="inner"
)

print("Inner Join Result:")
print(inner_join_df)

# %% [markdown]
# ### Left Join
# A left join returns all rows from the left dataframe and matching rows from the right dataframe. If there is no match, the right side will contain null values.

# %%
# Left join example
left_join_df = employees_df.join(
    departments_df,
    left_on="department_id",
    right_on="department_id",
    how="left"
)

print("Left Join Result:")
print(left_join_df)

# %% [markdown]
# ### Anti Join
# An anti join returns only the rows from the left dataframe that do not have a match in the right dataframe.

# %%
# Anti join example
# First, let's create a modified employees dataframe with some unmatched records
modified_employees_df = pl.DataFrame({
    "employee_id": [1, 2, 3, 4, 5, 6, 7],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
    "department_id": [101, 102, 101, 103, 102, 105, 106]  # 105 and 106 don't exist in departments_df
})

anti_join_df = modified_employees_df.join(
    departments_df,
    left_on="department_id",
    right_on="department_id",
    how="anti"
)

print("Anti Join Result (employees without matching departments):")
print(anti_join_df)

# %% [markdown]
# ## 3. Aggregation Expressions

# %% [markdown]
# ### Basic Aggregations

# %%
# Create a sample dataframe for aggregation examples
sales_df = pl.DataFrame({
    "product_id": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "category": ["A", "A", "B", "B", "C", "A", "A", "B", "B", "C"],
    "region": ["North", "North", "South", "South", "East", "North", "North", "South", "South", "East"],
    "sales_amount": [100, 150, 200, 250, 300, 120, 180, 220, 270, 320],
    "quantity": [5, 3, 4, 5, 6, 6, 4, 5, 6, 7]
})

print("Sales DataFrame:")
print(sales_df)

# %% [markdown]
# ### Simple Aggregations

# %%
# Calculate total sales and average quantity by category
category_agg = sales_df.groupby("category").agg([
    pl.col("sales_amount").sum().alias("total_sales"),
    pl.col("quantity").mean().alias("avg_quantity")
])

print("Aggregation by Category:")
print(category_agg)

# %% [markdown]
# ### Multiple Aggregations

# %%
# Calculate multiple statistics by region
region_agg = sales_df.groupby("region").agg([
    pl.col("sales_amount").sum().alias("total_sales"),
    pl.col("sales_amount").mean().alias("avg_sales"),
    pl.col("sales_amount").max().alias("max_sales"),
    pl.col("sales_amount").min().alias("min_sales"),
    pl.col("quantity").sum().alias("total_quantity")
])

print("Aggregation by Region:")
print(region_agg)

# %% [markdown]
# ### Complex Aggregations with Window Functions

# %%
# Calculate running totals and percentages
sales_with_totals = sales_df.with_columns([
    pl.col("sales_amount").sum().over("category").alias("category_total"),
    pl.col("sales_amount").sum().over("region").alias("region_total"),
    (pl.col("sales_amount") / pl.col("sales_amount").sum().over("category") * 100).alias("category_percentage")
])

print("Sales with Running Totals and Percentages:")
print(sales_with_totals)

# %% [markdown]
# ## 4. Date and Time Expressions

# %% [markdown]
# ### Creating Date/Time Data

# %%
# Create a sample dataframe with date/time data
dates_df = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "date": [
        datetime.datetime(2023, 1, 1),
        datetime.datetime(2023, 2, 15),
        datetime.datetime(2023, 3, 30),
        datetime.datetime(2023, 4, 10),
        datetime.datetime(2023, 5, 20)
    ],
    "timestamp": [
        datetime.datetime(2023, 1, 1, 10, 30, 45),
        datetime.datetime(2023, 2, 15, 14, 20, 10),
        datetime.datetime(2023, 3, 30, 9, 15, 30),
        datetime.datetime(2023, 4, 10, 16, 45, 20),
        datetime.datetime(2023, 5, 20, 11, 10, 5)
    ]
})

print("Dates DataFrame:")
print(dates_df)

# %% [markdown]
# ### Date/Time Operations

# %%
# Extract date components and perform date calculations
dates_operations = dates_df.with_columns([
    pl.col("date").dt.year().alias("year"),
    pl.col("date").dt.month().alias("month"),
    pl.col("date").dt.day().alias("day"),
    pl.col("date").dt.day_of_week().alias("day_of_week"),
    pl.col("date").dt.quarter().alias("quarter"),
    pl.col("date").dt.week().alias("week"),
    pl.col("date").dt.weekday().alias("weekday"),
    pl.col("date").dt.iso_year().alias("iso_year"),
    pl.col("date").dt.iso_week().alias("iso_week"),
    pl.col("date").dt.iso_weekday().alias("iso_weekday"),
    pl.col("date").dt.is_leap_year().alias("is_leap_year"),
    pl.col("date").dt.days_in_month().alias("days_in_month"),
    pl.col("date").dt.offset_by("1 month").alias("date_plus_1_month"),
    pl.col("date").dt.offset_by("-1 week").alias("date_minus_1_week")
])

print("Date Operations:")
print(dates_operations)

# %% [markdown]
# ### Time Operations

# %%
# Extract time components and perform time calculations
time_operations = dates_df.with_columns([
    pl.col("timestamp").dt.hour().alias("hour"),
    pl.col("timestamp").dt.minute().alias("minute"),
    pl.col("timestamp").dt.second().alias("second"),
    pl.col("timestamp").dt.microsecond().alias("microsecond"),
    pl.col("timestamp").dt.time().alias("time"),
    pl.col("timestamp").dt.offset_by("2 hours").alias("timestamp_plus_2_hours"),
    pl.col("timestamp").dt.offset_by("-30 minutes").alias("timestamp_minus_30_minutes")
])

print("Time Operations:")
print(time_operations)

# %% [markdown]
# ### Date Formatting

# %%
# Format dates in different ways
date_formatting = dates_df.with_columns([
    pl.col("date").dt.strftime("%Y-%m-%d").alias("formatted_date"),
    pl.col("date").dt.strftime("%d/%m/%Y").alias("formatted_date_dmy"),
    pl.col("date").dt.strftime("%B %d, %Y").alias("formatted_date_long"),
    pl.col("timestamp").dt.strftime("%Y-%m-%d %H:%M:%S").alias("formatted_timestamp")
])

print("Date Formatting:")
print(date_formatting)

# %% [markdown]
# ## 5. String Expressions

# %% [markdown]
# ### Creating String Data

# %%
# Create a sample dataframe with string data
strings_df = pl.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["John Smith", "Jane Doe", "Robert Johnson", "Emily Davis", "Michael Brown"],
    "email": ["john.smith@example.com", "jane.doe@example.com", "robert.j@example.com", "emily.d@example.com", "michael.b@example.com"],
    "address": ["123 Main St, New York, NY", "456 Oak Ave, Los Angeles, CA", "789 Pine Rd, Chicago, IL", "321 Elm St, Houston, TX", "654 Maple Dr, Phoenix, AZ"]
})

print("Strings DataFrame:")
print(strings_df)

# %% [markdown]
# ### Basic String Operations

# %%
# Basic string operations
string_basic = strings_df.with_columns([
    pl.col("name").str.to_uppercase().alias("name_upper"),
    pl.col("name").str.to_lowercase().alias("name_lower"),
    pl.col("name").str.lengths().alias("name_length"),
    pl.col("name").str.slice(0, 5).alias("name_first_5"),
    pl.col("name").str.slice(-5, None).alias("name_last_5")
])

print("Basic String Operations:")
print(string_basic)

# %% [markdown]
# ### String Pattern Matching

# %%
# String pattern matching
string_pattern = strings_df.with_columns([
    pl.col("email").str.contains("@").alias("has_at"),
    pl.col("email").str.contains(".com").alias("has_com"),
    pl.col("email").str.contains("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$").alias("valid_email"),
    pl.col("address").str.contains("New York").alias("in_new_york"),
    pl.col("address").str.contains("CA|NY|TX").alias("in_target_states")
])

print("String Pattern Matching:")
print(string_pattern)

# %% [markdown]
# ### String Splitting and Joining

# %%
# String splitting and joining
string_split_join = strings_df.with_columns([
    pl.col("name").str.split(" ").alias("name_parts"),
    pl.col("email").str.split("@").alias("email_parts"),
    pl.col("address").str.split(",").alias("address_parts")
])

# Extract parts from split results
string_extract = string_split_join.with_columns([
    pl.col("name_parts").list.get(0).alias("first_name"),
    pl.col("name_parts").list.get(1).alias("last_name"),
    pl.col("email_parts").list.get(0).alias("email_username"),
    pl.col("email_parts").list.get(1).alias("email_domain"),
    pl.col("address_parts").list.get(0).alias("street"),
    pl.col("address_parts").list.get(1).alias("city"),
    pl.col("address_parts").list.get(2).alias("state")
])

print("String Splitting and Extraction:")
print(string_extract)

# %% [markdown]
# ### String Replacement

# %%
# String replacement
string_replace = strings_df.with_columns([
    pl.col("email").str.replace("@", " [at] ").alias("email_obfuscated"),
    pl.col("address").str.replace("St", "Street").alias("address_expanded"),
    pl.col("address").str.replace("Ave", "Avenue").alias("address_expanded"),
    pl.col("address").str.replace("Rd", "Road").alias("address_expanded"),
    pl.col("address").str.replace("Dr", "Drive").alias("address_expanded")
])

print("String Replacement:")
print(string_replace)

# %% [markdown]
# ## 6. Data Export

# %% [markdown]
# ### Export to CSV

# %%
# Export to CSV
# Uncomment to actually write the file
# sales_df.write_csv(DATA_DIR / "sales_export.csv")

print("CSV Export Example (commented out):")
print("sales_df.write_csv(DATA_DIR / 'sales_export.csv')")

# %% [markdown]
# ### Export to Parquet

# %%
# Export to Parquet
# Uncomment to actually write the file
# sales_df.write_parquet(DATA_DIR / "sales_export.parquet")

print("Parquet Export Example (commented out):")
print("sales_df.write_parquet(DATA_DIR / 'sales_export.parquet')")

# %% [markdown]
# ### Export to Excel

# %%
# Export to Excel
# Uncomment to actually write the file
# sales_df.write_excel(DATA_DIR / "sales_export.xlsx")

print("Excel Export Example (commented out):")
print("sales_df.write_excel(DATA_DIR / 'sales_export.xlsx')")

# %% [markdown]
# ### Export to JSON

# %%
# Export to JSON
# Uncomment to actually write the file
# sales_df.write_json(DATA_DIR / "sales_export.json")

print("JSON Export Example (commented out):")
print("sales_df.write_json(DATA_DIR / 'sales_export.json')")

# %% [markdown]
# ### Export with Custom Options

# %%
# Export with custom options
# Uncomment to actually write the file
# sales_df.write_csv(
#     DATA_DIR / "sales_export_custom.csv",
#     separator=";",
#     quote_char='"',
#     null_value="NULL",
#     date_format="%Y-%m-%d",
#     datetime_format="%Y-%m-%d %H:%M:%S",
#     float_precision=2
# )

print("Custom CSV Export Example (commented out):")
print("""
sales_df.write_csv(
    DATA_DIR / "sales_export_custom.csv",
    separator=";",
    quote_char='"',
    null_value="NULL",
    date_format="%Y-%m-%d",
    datetime_format="%Y-%m-%d %H:%M:%S",
    float_precision=2
)
""") 
