# %% [markdown]
# # Regression using Keras
#
# This notebook demonstrates how to use a simple Keras (TensorFlow backend) neural network for a **regression task**. We will follow a similar workflow as the previous Scikit-learn example: data loading, exploratory data analysis (EDA), data splitting, feature scaling, model building, training, validation, and final evaluation on a test set.
#
# ## Import Necessary Libraries
#
# We begin by importing all the tools we'll need.
#
# *   **scikit-learn:** For datasets, splitting, scaling, and regression metrics.
# *   **polars:** For efficient data manipulation and exploration (EDA).
# *   **matplotlib & seaborn:** For creating informative visualizations.
# *   **keras:** For building and training the neural network model.
# *   **warnings:** To suppress potential clutter from library warnings.
#
#

# %%
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing # Using the same dataset for continuity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # Important for Neural Networks
from sklearn.metrics import (mean_squared_error, mean_absolute_error,
                             r2_score) # Regression metrics
import keras
from keras import layers

import warnings

# Configure visualization style and ignore warnings for cleaner output
sns.set_theme(style="whitegrid")
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)

print(f"Keras Version: {keras.__version__}")


# %% [markdown]
# ## Load and Prepare the Dataset
#
# We load the California Housing dataset from scikit-learn. This dataset contains features about census block groups in California, and the target variable is the median house value for that block group (a continuous value suitable for regression). We convert it into a Polars DataFrame for EDA.
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

print("Feature names:", feature_names)

# Create a Polars DataFrame
df = pl.from_numpy(X,
                   schema=feature_names,
                  ).with_columns(
    pl.Series(name="MedHouseVal", values=y) # Target column name
)

print("\nDataset loaded and converted to Polars DataFrame:")
print(f"Shape of the DataFrame: {df.shape}")
print("\nFirst 5 rows of the DataFrame:")
print(df.head())
print("\nTarget variable description: Median house value in $100,000s")


# %% [markdown]
# ## Exploratory Data Analysis (EDA) with Polars
#
# We perform the same checks as before:
#
# *   **Basic statistics:** Distribution of features and target.
# *   **Missing values:** Check for completeness.
# *   **Target distribution:** Examine the distribution of median house values.
# *   **Visualizations:** Histograms and scatter plots to see feature distributions and relationships with the target.
#
# *Do not forget that EDA is independent of the modeling library.*
#

# %%
print("\n--- Exploratory Data Analysis ---")

# Basic statistics
print("\nBasic Descriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values Check:")
print(df.null_count()) # Expecting all zeros

# Target variable distribution
print("\nTarget Variable Distribution (MedHouseVal):")
plt.figure(figsize=(8, 5))
sns.histplot(df['MedHouseVal'].to_numpy(), kde=True)
plt.title('Distribution of Median House Value (Target)')
plt.xlabel('Median House Value ($100,000s)')
plt.ylabel('Frequency')
plt.show()

# Feature vs Target Scatter Plot (Example: MedInc vs MedHouseVal)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df.to_pandas(), x='MedInc', y='MedHouseVal', alpha=0.5)
plt.title('Median Income vs. Median House Value')
plt.xlabel('Median Income ($10,000s)')
plt.ylabel('Median House Value ($100,000s)')
plt.show()


# %% [markdown]
#
# ## Data Splitting (Train, Validation, Test)
#
#
# We split the data into training, validation, and test sets using the same 60%/20%/20% ratio as before. `random_state` ensures reproducibility.

# %%
import random


# %%
# Separate features (X) and target (y)
# X = df.select(pl.col(feature_names)).to_numpy()
# y = df.select(pl.col("MedHouseVal")).to_numpy().ravel()

# First split: Separate out the Test set (20%)
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Second split: Split the remaining into Training (60%) and Validation (20%)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42 # 0.25 * 0.80 = 0.20
)

print("\n--- Data Splitting ---")
print(f"Training set size: {X_train.shape[0]} samples ({X_train.shape[0]/X.shape[0]:.0%})")
print(f"Validation set size: {X_val.shape[0]} samples ({X_val.shape[0]/X.shape[0]:.0%})")
print(f"Test set size: {X_test.shape[0]} samples ({X_test.shape[0]/X.shape[0]:.0%})")

# %% [markdown]
# ## Feature Scaling
#
# Neural networks generally perform better when input features are on a similar scale. We use `StandardScaler` from Scikit-learn to scale the features (mean=0, std=1).
#
# **Important:** The scaler is `fit` **only** on the training data and then used to `transform` the training, validation, and test sets. This prevents data leakage from the validation and test sets into the training process.
#
# *   StandardScaler: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

# %%
print("\n--- Feature Scaling ---")

scaler = StandardScaler()

# Fit scaler only on the training data
scaler.fit(X_train)

# Transform all sets using the fitted scaler
X_train_scaled = scaler.transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

print("Features scaled using StandardScaler.")
print(f"Mean of scaled training features (should be approx 0): {X_train_scaled.mean(axis=0).round(2)}")
print(f"Std Dev of scaled training features (should be approx 1): {X_train_scaled.std(axis=0).round(2)}")


# %% [markdown]
#
# ## Define and Compile Keras Model
#
# We define a simple sequential neural network architecture using Keras:
#
# *   **Input Layer:** Implicitly defined by the `input_shape` in the first `Dense` layer. The shape corresponds to the number of features.
# *   **Hidden Layers:** Two `Dense` (fully connected) layers with ReLU activation function. ReLU is a common choice for hidden layers.
# *   **Output Layer:** A single `Dense` neuron with **no activation function** (or equivalently, a 'linear' activation). This is standard for regression problems, as we want to predict a continuous value without constraining its range like sigmoid or ReLU would.
#
# After defining the architecture, we **compile** the model, specifying:
# *   **Loss function:** `mean_squared_error` (MSE) is a standard loss for regression.
# *   **Optimizer:** `adam` is a popular and generally effective optimization algorithm.
# *   **Metrics:** We'll monitor `mae` (Mean Absolute Error) and `mse` (Mean Squared Error) during training and evaluation.
#

# %%
print("\n--- Define and Compile Keras Model ---")

# Get the number of features from the scaled training data shape
n_features = X_train_scaled.shape[1]

def build_model(input_shape):
    model = keras.Sequential(
        [
            layers.Input(shape=(input_shape,)), # Define input shape explicitly
            layers.Dense(10, activation="relu", name="hidden_layer_1"),
            layers.Dense(10, activation="relu", name="hidden_layer_2"),
            layers.Dense(1, name="output_layer"), # Linear activation for regression output
        ]
    )
    # Compile the model
    optimizer = keras.optimizers.Adam(learning_rate=0.001)
    model.compile(loss="mse", # Mean Squared Error loss
                  optimizer=optimizer,
                  metrics=["mae", "mse"]) # Monitor Mean Absolute Error and MSE
    return model

model = build_model(n_features)

# Display model architecture
print("Model Summary:")
model.summary()


# %% [markdown]
#
# ## Train the Model
#
# We train the model using the `fit` method on the *scaled training data* (`X_train_scaled`, `y_train`).
#
# Key parameters for `fit`:
# *   `epochs`: The number of times the model will iterate over the entire training dataset.
# *   `batch_size`: The number of samples processed before the model's weights are updated.
# *   `validation_data`: Data on which to evaluate the loss and any model metrics at the end of each epoch. We use the *scaled validation set* (`X_val_scaled`, `y_val`).
# *   `verbose`: Controls the verbosity of the training output (0=silent, 1=progress bar, 2=one line per epoch).
#
# The `fit` method returns a `History` object containing the training and validation loss/metrics for each epoch.

# %%
print("\n--- Train the Model ---")

# Set training parameters
EPOCHS = 30 # Maximum number of epochs
BATCH_SIZE = 32

# Train the model
history = model.fit(
    X_train_scaled,
    y_train,
    epochs=EPOCHS,
    batch_size=BATCH_SIZE,
    validation_data=(X_val_scaled, y_val),
    verbose=1 # Show progress bar
)

print("\nModel training complete.")


# %% [markdown]
# ## Visualize Training History (Validation)
#
# We plot the training and validation loss (MSE) and metrics (MAE) over the epochs using the `history` object returned by `model.fit()`. This helps visualize:
#
# *   **Convergence:** Whether the model's performance improved over time.
# *   **Overfitting:** If the training loss continues to decrease while the validation loss starts to increase or plateaus significantly higher, the model is likely overfitting. Early stopping helps mitigate this.
#

# %%
print("\n--- Visualize Training History ---")

history_df = pl.DataFrame(history.history)
history_df = history_df.with_columns(pl.Series(name="epoch", values=np.arange(1, len(history_df) + 1)))

print(f"Training stopped after {len(history_df)} epochs.")
print("\nTraining History DataFrame (metrics per epoch):")
print(history_df.tail()) # Show last few epochs

# Plotting function
def plot_history(history_df, metrics=('loss', 'mae')):
    plt.figure(figsize=(12, 5 * len(metrics)))
    num_epochs = len(history_df)

    for i, metric in enumerate(metrics):
        plt.subplot(len(metrics), 1, i + 1)
        plt.plot(history_df['epoch'], history_df[metric], label=f'Training {metric.upper()}')
        plt.plot(history_df['epoch'], history_df[f'val_{metric}'], label=f'Validation {metric.upper()}', linestyle='--')
        plt.xlabel('Epoch')
        plt.ylabel(metric.upper())
        min_val_epoch = history_df[f'val_{metric}'].arg_min() + 1 # Polars uses 0-based index
        min_val_score = history_df[f'val_{metric}'].min()
        plt.title(f'Training and Validation {metric.upper()}')
        plt.scatter(min_val_epoch, min_val_score, color='red', zorder=5, label=f'Best Val {metric.upper()} (Epoch {min_val_epoch})')
        plt.legend()
        plt.grid(True)

    plt.tight_layout()
    plt.show()

plot_history(history_df, metrics=['loss', 'mae']) # 'loss' is MSE here

print("Training history plots displayed.")

# %% [markdown]
# ## Evaluate Model on Validation Set
#
# We explicitly evaluate the final model (with the best weights restored) on the validation set using `model.evaluate()`. This gives us the final MSE and MAE on the data used for selecting the best epoch.
#
# *   Keras Evaluation: https://keras.io/api/models/model_training_apis/#evaluate-method

# %%
print("\n--- Model Evaluation on Validation Set ---")

val_loss, val_mae, val_mse = model.evaluate(X_val_scaled, y_val, verbose=0)

# Calculate RMSE from MSE
val_rmse = np.sqrt(val_mse)
# Calculate R2 score using scikit-learn based on predictions
y_pred_val = model.predict(X_val_scaled).flatten()
val_r2 = r2_score(y_val, y_pred_val)


print("\nValidation Set Performance (Best Epoch):")
print(f"Mean Squared Error (MSE): {val_mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {val_rmse:.4f}")
print(f"Mean Absolute Error (MAE): {val_mae:.4f}")
print(f"R-squared (R²): {val_r2:.4f}")


# %% [markdown]
#
# ## Final Test Evaluation
#
# Now we evaluate the trained model on the *Test Set* (`X_test_scaled`, `y_test`), which the model has never seen before. This provides the most realistic estimate of the model's performance on new, unseen data.
#
# We calculate the final regression metrics (MSE, RMSE, MAE, R²) on the test set predictions. We also visualize the performance by plotting true values against predicted values. Ideally, points should lie close to the diagonal line y=x.
#

# %%

print("\n--- Final Test Evaluation ---")

# Evaluate the model on the Test Set
test_loss, test_mae, test_mse = model.evaluate(X_test_scaled, y_test, verbose=0)

# Calculate RMSE from MSE
test_rmse = np.sqrt(test_mse)
# Make predictions on the test set to calculate R2
y_pred_test = model.predict(X_test_scaled).flatten() # Flatten output for metrics
test_r2 = r2_score(y_test, y_pred_test)

print("\n--- Final Test Set Performance ---")
print(f"Test Mean Squared Error (MSE): {test_mse:.4f}")
print(f"Test Root Mean Squared Error (RMSE): {test_rmse:.4f}")
print(f"Test Mean Absolute Error (MAE): {test_mae:.4f}")
print(f"Test R-squared (R²): {test_r2:.4f}")


# Plot True vs. Predicted values for the test set
print("\nPlotting True vs. Predicted Values on Test Set...")
plt.figure(figsize=(8, 8))
plt.scatter(y_test, y_pred_test, alpha=0.4)
# Add the ideal y=x line
min_val = min(np.min(y_test), np.min(y_pred_test))
max_val = max(np.max(y_test), np.max(y_pred_test))
plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Ideal (y=x)')
plt.xlabel("True Values (Median House Value)")
plt.ylabel("Predicted Values (Median House Value)")
plt.title(f"Keras Model - True vs. Predicted Values on Test Set (R²: {test_r2:.3f})")
plt.legend()
plt.grid(True)
plt.axis('equal') # Ensure x and y axes have the same scale
plt.tight_layout()
plt.show()

print("\nFinal evaluation complete.")

# Interpretation: The test set metrics (R², RMSE, MAE) indicate the model's expected
# performance on new data. Compare these to the validation metrics; similar scores suggest
# good generalization. The scatter plot provides a visual check of prediction accuracy
# across the range of target values. Points clustering tightly around the red diagonal
# line indicate better performance.

# %%
