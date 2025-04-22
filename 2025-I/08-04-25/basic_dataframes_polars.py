# %% [markdown]
# # Reading Data with Polars
# This notebook demonstrates how to read different data formats using Polars, including both eager and lazy APIs.

# %% [markdown]
# For this we have to be sure that we have polars and pyarrow installed in our environment.
# ```sh
# pip install polars
# pip install pyarrow
# ```

# %% [markdown]
# ## Imports and Setup

# %%
import polars as pl
from pathlib import Path

# Define the data directory path
DATA_DIR = Path("data")

# %% [markdown]
# ## 1. Reading CSV Files

# %% [markdown]
# ### Conventional (Eager) API

# %%
# Reading CSV with conventional API
df_csv = pl.read_csv(
    DATA_DIR / "dataset.csv",
    separator=",",  # The delimiter to use for CSV files
    has_header=True,  # Whether the CSV file has a header row
    ignore_errors=False,  # Whether to ignore parsing errors
    encoding="utf8",  # The encoding of the file
    quote_char='"',  # The character used for quoting fields
    infer_schema_length=100,  # Number of rows to use for schema inference
)

# Display basic information
print("\nCSV DataFrame Info:")
df_csv
# df_csv.describe()

# %% [markdown]
# ## 2. Reading Parquet Files

# %% [markdown]
# ### Conventional (Eager) API

# %%
# Reading Parquet with conventional API
df_parquet = pl.read_parquet(
    DATA_DIR / "dataset.parquet",
    columns=None,  # List of column names to read (None for all columns)
    row_index_name=None,  # Name of the row count column if present
    row_index_offset=0,  # Offset for row count if present
    use_pyarrow=True,  # Whether to use pyarrow for reading
    memory_map=True,  # Whether to memory map the file
)

# Display basic information
print("\nParquet DataFrame Info:")
print(df_parquet.describe())

# %% [markdown]
# ## 3. Reading Feather Files

# %% [markdown]
# ### Conventional (Eager) API

# %%
# Reading Feather with conventional API
df_feather = pl.read_ipc(
    DATA_DIR / "dataset.feather",
    columns=None,  # List of column names to read (None for all columns)
    memory_map=True,  # Whether to memory map the file. This allows to read bigger than memory files.
)

# Display basic information
print("\nFeather DataFrame Info:")
print(df_feather.describe())

# %% [markdown]
# ### Lazy API

# %%
df_parquet.head()

# %%
# Reading CSV with lazy API
lazy_df_csv = pl.scan_csv(
    DATA_DIR / "dataset.csv",
    separator=",",
    has_header=True,
    ignore_errors=False,
    encoding="utf8",
    quote_char='"',
    infer_schema_length=100,
)

# Example of executing a lazy query, we will explain it later...
lazy_result = (
    lazy_df_csv
    .filter(pl.col("Age") > 26)  # Example filter
    .group_by(by="Product Category")
    .agg(
        pl.col("Price per Unit").mean().alias("mean_price"),
        pl.col("Total Amount").sum().alias("total")
    )
)

# lazy_result is a lazy object that contains the graph of operations, is not computed yet
lazy_result
# Execute the lazy query
df_result = lazy_result.collect()
df_result

# %% [markdown]
# ## 4. Advanced Reading Examples

# %% [markdown]
# ### Reading with Schema Specification

# %%
df_feather.head(10)

# %%

# %%
# Define a custom schema
schema = {
        'Transaction ID': pl.Int64,
        'Date': pl.Date,
        'Customer ID': pl.String,
        'Gender': pl.String,
        'Age': pl.Int64,
        'Product Category': pl.String,
        'Quantity': pl.Int64,
        'Price per Unit': pl.Int64,
        'Total Amount': pl.Int64
}

# Read CSV with explicit schema
df_with_schema = pl.read_csv(
    DATA_DIR / "dataset.csv",
    schema=schema,  # Specify the schema explicitly
    infer_schema_length=0,  # Disable schema inference when schema is provided
)

# %%
df_with_schema.head(10)

# %% [markdown]
# ## About Null Values

# %%
df_with_schema.null_count()

# %%
df_with_schema.drop_nulls()

# %% [markdown]
# ## 5. Data Manipulation with Polars

# %% [markdown]
# ### Select Context
# The `select` context allows you to choose specific columns and apply operations to them.

# %%
# Basic select operations

# %%
df = df_with_schema
df.head(4)

# %%
df = df_with_schema

# Basic column selection
selected_cols = df.select(["Product Category", "Quantity", "Customer ID"])
print("Selected columns:")
print(selected_cols)

# %%
df.head()


# %%

# Select with expressions
selected_expr = df.select([
    pl.col("Customer ID"),
    pl.col("Transaction ID").alias("id"),
    ((pl.col("Total Amount") / pl.col("Price per Unit")) *10).alias("price"),
    pl.col("Age").cast(pl.Float64).alias("age_float")
                ])
print("\nSelected with expressions:")
print(selected_expr)

# %%

# Select with conditional expressions
selected_cond = df.select([
    pl.col("Transaction ID"),
    pl.col("Customer ID"),
    pl.when(pl.col("Age") > 35).then(pl.lit("Senior")).otherwise(pl.lit("Junior")).alias("age_category")
])
print("\nSelected with conditional expressions:")
print(selected_cond)
# %%
df.select(pl.col('Product Category').unique())

# %%
# Select with aggregations
selected_agg = df.group_by(by='Product Category').agg(
    pl.col("Total Amount").mean().alias("avg_amount"),
    pl.col("Age").max().alias("max_age")
)
print("\nSelected with aggregations:")
print(selected_agg)

# %% [markdown]
# ### Filter Context
# The `filter` context allows you to filter rows based on conditions.

# %%
df.head(2)

# %%
# Basic filtering
filtered_basic = df.filter(pl.col("Age") > 30)
print("Filtered by age > 30:")
filtered_basic
# %%
# Filter with multiple conditions
filtered_multi = df.filter(
    (pl.col("Age") > 30) & (pl.col("Total Amount") > 100)
)
print("\nFiltered by age > 30 AND total amount > 100:")
print(filtered_multi)

# %%

# Filter with OR conditions
filtered_or = df.filter(
    (pl.col("Product Category") == "Electronics") | (pl.col("Product Category") == "Clothing")
)
print("\nFiltered by product category Electronics OR Clothing:")
print(filtered_or)

# %%
# Filter with string operations
filtered_str = df.filter(
    pl.col("Gender").str.contains("F")
)
print("\nFiltered by gender containing 'F':")
print(filtered_str)
# %%
# Filter with is_in
filtered_in = df.filter(
    pl.col("Product Category").is_in(["Electronics","Books"])
)
print("\nFiltered by product category in Electronics, Clothing, or Books:")
print(filtered_in)

# %% [markdown]
# ### With_columns Context
# The `with_columns` context allows you to add or modify columns while keeping all existing columns.

# %%
# Basic with_columns
with_cols_basic = df.with_columns([
    (pl.col("Total Amount") / pl.col("Quantity")).alias("avg_price_per_item"),
    pl.col("Age").cast(pl.Float64).alias("age_float")
])
print("Added avg_price_per_item and age_float columns:")
print(with_cols_basic)

# %%

# With_columns with conditional expressions
with_cols_cond = df.with_columns([
    pl.when(pl.col("Age") > 35).then(pl.lit("Senior")).otherwise(pl.lit("Junior")).alias("age_category"),
    pl.when(pl.col("Total Amount") > 500).then(pl.lit("High")).otherwise(pl.lit("Medium")).alias("purchase_level")
])
print("\nAdded age_category and purchase_level columns:")
print(with_cols_cond)

# %%

# With_columns with string operations
with_cols_str = df.with_columns([
    pl.col("Customer ID").str.to_uppercase().alias("customer_id_upper"),
    pl.col("Customer ID").str.len_chars().alias("customer_id_length")
])
print("\nAdded customer_id_upper and customer_id_length columns:")
print(with_cols_str)

# %%

# With_columns with window functions
with_cols_window = df.with_columns([
    pl.col("Total Amount").rank().over("Product Category").alias("amount_rank_in_category"),
    pl.col("Age").mean().over("Product Category").alias("avg_age_in_category")
])
print("\nAdded amount_rank_in_category and avg_age_in_category columns:")
print(with_cols_window)

# %% [markdown]
# ### Combining Operations
# Polars allows you to chain multiple operations together for complex data transformations.

# %%
# Combining select, filter, and with_columns
complex_transform = (
    df_csv
    .with_columns([
        (pl.col("Total Amount") / pl.col("Quantity")).alias("avg_price_per_item"),
        pl.when(pl.col("Age") > 35).then(pl.lit("Senior")).otherwise(pl.lit("Junior")).alias("age_category")
    ])
    .filter(pl.col("Product Category").is_in(["Electronics", "Clothing"]))
    .select([
        pl.col("Transaction ID"),
        pl.col("Customer ID"),
        pl.col("Product Category"),
        pl.col("avg_price_per_item"),
        pl.col("age_category")
    ])
)
print("Complex transformation combining multiple operations:")
print(complex_transform)


# %%
complex_transform.write_excel('data/new_data.xlsx')

# %%
# !pip install xlsxwriter

# %%
complex_transform.write_
