# %% [markdown]
# # Regression Model Examples using Scikit-learn and Polars
#
# This notebook demonstrates how to use various machine learning models for a **regression task** (predicting a continuous numerical value). We will follow a standard workflow: data loading, exploratory data analysis (EDA), data splitting, model training, validation, comparison, and final evaluation on a test set.
#
# ## Import Necessary Libraries
#
# We begin by importing all the tools we'll need.
#
# *   **scikit-learn:** For datasets, model implementations, splitting, and regression metrics.
# *   **polars:** For efficient data manipulation and exploration (EDA).
# *   **matplotlib & seaborn:** For creating informative visualizations.
# *   **warnings:** To suppress potential clutter from library warnings.
#
#

# %%
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing # Changed to a regression dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge # Regression models
from sklearn.tree import DecisionTreeRegressor          # Regression model
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor # Regression models
from sklearn.metrics import (mean_squared_error, mean_absolute_error,
                             r2_score) # Regression metrics
import warnings

# Configure visualization style and ignore warnings for cleaner output
sns.set_theme(style="whitegrid")
warnings.filterwarnings('ignore', category=FutureWarning) # Ignore specific future warnings from libraries
warnings.filterwarnings('ignore', category=UserWarning)   # Ignore specific user warnings



# %% [markdown]
# ## Load and Prepare the Dataset
#
# We load the California Housing dataset from scikit-learn. This is a classic dataset for regression tasks, containing features about census block groups in California and the target variable being the median house value for that block group. We then convert it into a Polars DataFrame for easier manipulation during EDA.
#
# *   Scikit-learn Datasets: https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset
# *   Polars DataFrame: https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html
#
#

# %%
# Load the dataset
housing = fetch_california_housing()
X = housing.data
y = housing.target # Target is median house value (continuous)
feature_names = housing.feature_names
# No target_names for regression, the target is continuous

print("Feature names:", feature_names)

# Create a Polars DataFrame
# We combine the features (X) and the target (y) into one DataFrame
df = pl.from_numpy(X,
                   schema=feature_names,
                  ).with_columns(
    pl.Series(name="MedHouseVal", values=y) # Target column name from dataset description
)

print("\nDataset loaded and converted to Polars DataFrame:")
print(f"Shape of the DataFrame: {df.shape}")
print("\nFirst 5 rows of the DataFrame:")
print(df.head())
print("\nTarget variable description: Median house value in $100,000s")


# %% [markdown]
# ## Exploratory Data Analysis (EDA) with Polars
#
# EDA is crucial to understand the data before modeling. We'll check:
#
# *   **Basic statistics:** Get a sense of the distribution of each feature and the target variable.
# *   **Missing values:** Identify if any data imputation is needed.
# *   **Target distribution:** Examine the distribution of the median house values (our target). Is it skewed? Are there outliers?
# *   **Visualizations:** Use pair plots (optional, can be slow for many features) and histograms/scatter plots to visualize relationships between features and the target variable.
#
# Importance of EDA: https://towardsdatascience.com/exploratory-data-analysis-eda-python-87178e35b14
#

# %%
print("\n--- Exploratory Data Analysis ---")

# Basic statistics
print("\nBasic Descriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values Check:")
print(df.null_count())
# Interpretation: A count of 0 means no missing values in any column.

# Target variable distribution
print("\nTarget Variable Distribution (MedHouseVal):")
plt.figure(figsize=(8, 5))
sns.histplot(df['MedHouseVal'].to_numpy(), kde=True)
plt.title('Distribution of Median House Value (Target)')
plt.xlabel('Median House Value ($100,000s)')
plt.ylabel('Frequency')
plt.show()
# Interpretation: Check for skewness, modality, and potential outliers.
# The California housing target is known to be capped at the high end.

# Feature Distributions (Example: MedInc - Median Income)
plt.figure(figsize=(8, 5))
sns.histplot(df['MedInc'].to_numpy(), kde=True)
plt.title('Distribution of Median Income (Feature)')
plt.xlabel('Median Income ($10,000s)')
plt.ylabel('Frequency')
plt.show()


# Feature vs Target Scatter Plot (Example: MedInc vs MedHouseVal)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df.to_pandas(), x='MedInc', y='MedHouseVal', alpha=0.5) # Convert for seaborn scatterplot
plt.title('Median Income vs. Median House Value')
plt.xlabel('Median Income ($10,000s)')
plt.ylabel('Median House Value ($100,000s)')
plt.show()
# Interpretation: Look for correlations or patterns between features and the target.
# Here, we generally expect higher income to correlate with higher house value.

# Optional: Pairplot (can be computationally expensive for many features)
# print("\nGenerating Pairplot (subset of features, requires Pandas conversion)...")
# df_pandas = df.select(['MedInc', 'HouseAge', 'AveRooms', 'Population', 'MedHouseVal']).to_pandas() # Select a subset
# pairplot_fig = sns.pairplot(df_pandas, diag_kind='kde', plot_kws={'alpha':0.3})
# pairplot_fig.fig.suptitle("Pairplot of Selected Features and Target", y=1.02)
# plt.show()
# print("Pairplot displayed.")

# %% [markdown]
#
# ## Data Splitting (Train, Validation, Test)
#
#
# We split the data into three distinct sets:
#
# *  **Training Set:** Used to train the models. (e.g., 60% of data)
# *  **Validation Set:** Used to tune hyperparameters (if needed) and select the best model among the candidates. (e.g., 20% of data)
# *  **Test Set:** Used ONLY for the final evaluation of the chosen best model. This provides an unbiased estimate of the model's performance on unseen data.
#
# We use `train_test_split` twice. First, to separate the Test set. Second, to split the remaining data into Training and Validation sets.
# **Note:** `stratify=y` is generally *not* used for regression tasks as the target is continuous.
# `random_state` ensures reproducibility - the split will be the same every time.
#
# *   Train-Test Split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
#

# %%
# Separate features (X) and target (y) again if needed (though we have them from Step 2)
# X = df.select(pl.col(feature_names)).to_numpy() # Features
# y = df.select(pl.col("MedHouseVal")).to_numpy().ravel() # Target

# First split: Separate out the Test set (20% of the total data)
# No stratification for regression target
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Second split: Split the remaining data (X_train_val) into Training and Validation sets
# We want validation to be 20% of original, which is 25% of the remaining 80% (0.20 / 0.80 = 0.25)
# No stratification for regression target
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42
)

print("\n--- Data Splitting ---")
print(f"Original dataset size: {X.shape[0]} samples")
print(f"Training set size: {X_train.shape[0]} samples ({X_train.shape[0]/X.shape[0]:.0%})")
print(f"Validation set size: {X_val.shape[0]} samples ({X_val.shape[0]/X.shape[0]:.0%})")
print(f"Test set size: {X_test.shape[0]} samples ({X_test.shape[0]/X.shape[0]:.0%})")

# %% [markdown]
#
# ## Define and Train Models
#
# We define several regression models we want to compare:
#
# *  **Linear Regression:** The simplest linear model fitting a line/plane/hyperplane to the data.
# *  **Ridge Regression:** A linear model with L2 regularization to prevent overfitting by penalizing large coefficients.
# *  **Decision Tree Regressor:** A non-linear model that splits data based on feature thresholds to predict a target value (usually the mean of samples in a leaf).
# *  **Random Forest Regressor:** An ensemble method using multiple decision trees to improve robustness and accuracy, reducing overfitting compared to a single tree.
# *  **Gradient Boosting Regressor:** Another powerful ensemble method that builds trees sequentially, with each new tree trying to correct the errors of the previous ones.
#
# We then train each model using the `fit` method on the *Training set* (`X_train`, `y_train`).
# Basic logging (print statements) indicates the start and end of training for each model.
#
# *   Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
# *   Ridge: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
# *   Decision Tree Regressor: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
# *   Random Forest Regressor: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
# *   Gradient Boosting Regressor: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html
#

# %%

print("\n--- Model Training ---")

# Define models
# Setting random_state for reproducibility where applicable
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0, random_state=42), # Alpha is the regularization strength
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42, n_estimators=100, n_jobs=-1), # n_jobs=-1 uses all cores
    "Gradient Boosting": GradientBoostingRegressor(random_state=42, n_estimators=100)
}

# Dictionary to store trained models
trained_models = {}

# Train each model
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train, y_train)
    trained_models[name] = model
    print(f"{name} trained successfully.")

print("\nAll models trained.")
# %% [markdown]
#
# ## Model Validation
#
# Now we evaluate the trained models on the *Validation set* (`X_val`, `y_val`). This set was not used during training.
# We calculate key performance metrics for regression:
#
# *   **Mean Squared Error (MSE):** Average of the squared differences between predicted and actual values. Sensitive to large errors. Lower is better.
# *   **Root Mean Squared Error (RMSE):** Square root of MSE. Interpretable in the same units as the target variable. Lower is better.
# *   **Mean Absolute Error (MAE):** Average of the absolute differences between predicted and actual values. Less sensitive to outliers than MSE. Lower is better.
# *   **R-squared (R²):** Coefficient of determination. Represents the proportion of the variance in the dependent variable that is predictable from the independent variables. Ranges from -inf to 1. Higher is better (closer to 1). A value of 0 means the model performs no better than predicting the mean; negative values mean it performs worse.
#
# We will store these metrics for each model to compare them later.
#
# *   Regression Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics
#

# %%
print("\n--- Model Validation on Validation Set ---")

validation_results = []

for i, (name, model) in enumerate(trained_models.items()):
    print(f"\nValidating {name}...")

    # Make predictions on the validation set
    y_pred_val = model.predict(X_val)

    # Calculate metrics
    mse = mean_squared_error(y_val, y_pred_val)
    rmse = np.sqrt(mse) # Calculate RMSE from MSE
    mae = mean_absolute_error(y_val, y_pred_val)
    r2 = r2_score(y_val, y_pred_val)

    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")
    print(f"R-squared (R²): {r2:.4f}")

    # Store results for comparison plot
    validation_results.append({
        "Model": name,
        "MSE": mse,
        "RMSE": rmse,
        "MAE": mae,
        "R2": r2
    })


print("\nValidation complete.")

# Convert results to Polars DataFrame for easier handling later
results_df = pl.DataFrame(validation_results)
print("\nValidation Metrics Summary:")
# Display R2, RMSE, MAE which are often the most focused on
print(results_df.select(["Model", "R2", "RMSE", "MAE"]).sort("R2", descending=True))

# %% [markdown]
#
# ## Performance Comparison Visualization
#
# To easily compare the models, we visualize their performance metrics (R², RMSE, MAE) side-by-side using bar plots. This helps in identifying which model(s) performed best on the validation set according to different criteria.
#
# Note that MSE/RMSE/MAE have different scales than R². Lower is better for error metrics, while higher is better for R². We might plot them separately or choose one or two key metrics for the main comparison plot. Here, we'll plot R² and RMSE.
#
# We use Polars' `melt` function to reshape the DataFrame for easier plotting with Seaborn.
#
# *   Data Visualization: https://seaborn.pydata.org/tutorial/categorical.html
#

# %%

print("\n--- Performance Comparison Visualization ---")

# Melt the DataFrame to long format suitable for seaborn barplot
# We will plot R2 and RMSE side-by-side
metrics_to_plot = ["R2", "RMSE"]
results_melted_df = results_df.melt(
    id_vars="Model",
    value_vars=metrics_to_plot,
    variable_name="Metric",
    value_name="Score"
)

print("\nReshaped data for plotting:")
print(results_melted_df.head()) # Show head of melted data

# Create the bar plot using FacetGrid for separate y-axes if needed, or a single plot
# Single plot approach:
plt.figure(figsize=(14, 7))
barplot = sns.barplot(data=results_melted_df.to_pandas(), x="Model", y="Score", hue="Metric", palette="viridis") # Convert to pandas for seaborn
plt.title("Model Performance Comparison on Validation Set (R² and RMSE)")
plt.ylabel("Score")
plt.xlabel("Model")
# Adjust y-axis or use facets if scales are too different. Here R2 (0-1) and RMSE might differ significantly.
# We can add text labels for clarity
for container in barplot.containers:
    barplot.bar_label(container, fmt='%.3f', label_type='edge', padding=2)

# plt.ylim(0, 1.0) # Set limit for R2, but might clip RMSE, use carefully or remove
plt.legend(loc='best')
plt.xticks(rotation=15) # Slightly rotate x-axis labels if needed
plt.tight_layout()
plt.show()

print("Performance comparison plot displayed.")


# %% [markdown]
#
# ## Best Model Selection and Final Test Evaluation
#
# Based on the validation results (e.g., highest R² or lowest RMSE/MAE), we select the best-performing model.
#
# We now evaluate this chosen model on the *Test Set* (`X_test`, `y_test`), which the model has NEVER seen before (neither during training nor validation). This gives the most realistic estimate of how the model would perform on new, unseen data in a real-world scenario.
#
# We calculate the final regression metrics (MSE, RMSE, MAE, R²) on the test set. We also create a scatter plot comparing the true values (`y_test`) against the predicted values (`y_pred_test`). Ideally, points should lie close to the diagonal line y=x, indicating accurate predictions.
#
# *   Model Selection: https://scikit-learn.org/stable/model_selection.html
# *   Importance of Test Set: https://developers.google.com/machine-learning/crash-course/validation/check-your-intuition
#

# %%

print("\n--- Best Model Selection and Final Test Evaluation ---")

# Select the best model based on a chosen metric (e.g., highest R2)
# We sort the results DataFrame by R2 in descending order and pick the top one.
best_model_row = results_df.sort("R2", descending=True).row(0, named=True)
best_model_name = best_model_row['Model']
best_model = trained_models[best_model_name] # Retrieve the trained model object

print(f"Selected Best Model (based on Validation R²): {best_model_name}")
print(f"Validation R² of Best Model: {best_model_row['R2']:.4f}")
print(f"Validation RMSE of Best Model: {best_model_row['RMSE']:.4f}")


# Evaluate the best model on the Test Set
print(f"\nEvaluating {best_model_name} on the Test Set...")
y_pred_test = best_model.predict(X_test)

# Calculate final metrics on the test set
test_mse = mean_squared_error(y_test, y_pred_test)
test_rmse = np.sqrt(test_mse)
test_mae = mean_absolute_error(y_test, y_pred_test)
test_r2 = r2_score(y_test, y_pred_test)


print("\n--- Final Test Set Performance ---")
print(f"Test Mean Squared Error (MSE): {test_mse:.4f}")
print(f"Test Root Mean Squared Error (RMSE): {test_rmse:.4f}")
print(f"Test Mean Absolute Error (MAE): {test_mae:.4f}")
print(f"Test R-squared (R²): {test_r2:.4f}")


# Plot True vs. Predicted values for the test set
print("\nPlotting True vs. Predicted Values on Test Set...")
plt.figure(figsize=(8, 8))
plt.scatter(y_test, y_pred_test, alpha=0.3)
# Add the ideal y=x line
min_val = min(np.min(y_test), np.min(y_pred_test))
max_val = max(np.max(y_test), np.max(y_pred_test))
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Ideal (y=x)')
plt.xlabel("True Values (Median House Value)")
plt.ylabel("Predicted Values (Median House Value)")
plt.title(f"{best_model_name} - True vs. Predicted Values on Test Set")
plt.legend()
plt.grid(True)
plt.axis('equal') # Ensure x and y axes have the same scale for a proper y=x line
plt.show()

print("\nFinal evaluation complete.")



# %%

# %%
