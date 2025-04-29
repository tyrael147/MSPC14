# %% [markdown]
# ## Import Necessary Libraries
#
#
# We begin by importing all the tools we'll need.
#
# *   **scikit-learn:** For datasets, model implementations, splitting, and metrics.
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
from sklearn.datasets import load_raw, load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, ConfusionMatrixDisplay,
                             precision_recall_fscore_support)
import warnings

# Configure visualization style and ignore warnings for cleaner output
sns.set_theme(style="whitegrid")
warnings.filterwarnings('ignore', category=FutureWarning) # Ignore specific future warnings from libraries
warnings.filterwarnings('ignore', category=UserWarning)   # Ignore specific user warnings



# %% [markdown]
# ## Load and Prepare the Dataset
#
# We load the raw dataset from scikit-learn. This is a classic dataset for classification tasks, containing measurements for three species of raw flowers. We then convert it into a Polars DataFrame for easier manipulation during EDA.
#
# *   Scikit-learn Datasets: https://scikit-learn.org/stable/datasets/toy_dataset.html#raw-plants-dataset
# *   Polars DataFrame: https://pola-rs.github.io/polars/py-polars/html/reference/dataframe/index.html
#
#

# %%
raw.feature_names

# %%

# Load the dataset
# raw = load_iris()
raw = load_breast_cancer()
X = raw.data
y = raw.target
feature_names = raw.feature_names
target_names = raw.target_names

# Create a Polars DataFrame
# We combine the features (X) and the target (y) into one DataFrame
# We also add a column with the actual species names for better readability in EDA
df = pl.from_numpy(X,
                   schema=raw.feature_names.tolist(),
                  ).with_columns(
    pl.Series(name="target", values=y)
)
# Create a mapping from target index to target name
target_map = {str(i): name for i, name in enumerate(target_names)}

# Add the target names column using the mapping
df = df.with_columns(
    pl.col("target").cast(pl.Utf8).replace(target_map).alias("species_name")
)
print("Dataset loaded and converted to Polars DataFrame:")
print(f"Shape of the DataFrame: {df.shape}")
print("\nFirst 5 rows of the DataFrame:")
print(df.head())
print("\nTarget classes:", target_names)

# %% [markdown]
# ## Exploratory Data Analysis (EDA) with Polars
#
# EDA is crucial to understand the data before modeling. We'll check:
#
# *   **Basic statistics:** Get a sense of the distribution of each feature.
# *   **Missing values:** Identify if any data imputation is needed.
# *   **Class distribution:** See if the dataset is balanced or imbalanced.
# *   **Visualizations:** Use pair plots to visualize relationships between features and how they separate the classes.
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

# Class distribution
print("\nClass Distribution (Species Count):")
print(df.group_by("species_name").agg(pl.count().alias("count")))
# Interpretation: This shows how many samples belong to each raw species.
# An equal count suggests a balanced dataset, which simplifies modeling.

# Visualizations
# Pairplot to visualize relationships between features, colored by species
# Note: Seaborn's pairplot works well with Pandas DataFrames. We'll convert
# the Polars DataFrame temporarily just for this plot.
print("\nGenerating Pairplot (requires converting to Pandas temporarily)...")
df_pandas = df.to_pandas() # Convert Polars to Pandas for seaborn compatibility
pairplot_fig = sns.pairplot(df_pandas, hue='species_name', palette='viridis')
pairplot_fig.fig.suptitle("Pairplot of raw Features by Species", y=1.02) # Add title slightly above plot
plt.show()
print("Pairplot displayed.")
# Interpretation: The pairplot helps visualize how well different feature pairs
# can separate the classes. Look for clusters of colors (species) that are
# well-separated in certain plots (e.g., petal length vs. petal width).
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
# `stratify=y` ensures that the proportion of each class is roughly the same in all splits, which is important for classification tasks, especially with smaller or imbalanced datasets.
# `random_state` ensures reproducibility - the split will be the same every time.
#
# *   Train-Test Split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
# *   Stratification: https://scikit-learn.org/stable/modules/cross_validation.html#stratification
#

# %%
# Separate features (X) and target (y) again if needed (though we have them from Step 2)
# X = df.select(pl.col(feature_names)).to_numpy() # Features
# y = df.select(pl.col("target")).to_numpy().ravel() # Target

# First split: Separate out the Test set (20% of the total data)
X_train_val, X_test, y_train_val, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Second split: Split the remaining data (X_train_val) into Training and Validation sets
# We want validation to be 20% of original, which is 25% of the remaining 80% (0.20 / 0.80 = 0.25)
X_train, X_val, y_train, y_val = train_test_split(
    X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val
)

print("\n--- Data Splitting ---")
print(f"Original dataset size: {X.shape[0]} samples")
print(f"Training set size: {X_train.shape[0]} samples ({X_train.shape[0]/X.shape[0]:.0%})")
print(f"Validation set size: {X_val.shape[0]} samples ({X_val.shape[0]/X.shape[0]:.0%})")
print(f"Test set size: {X_test.shape[0]} samples ({X_test.shape[0]/X.shape[0]:.0%})")

# Verify stratification (optional check)
print("\nClass distribution in each set:")
print("Train:", np.bincount(y_train))
print("Validation:", np.bincount(y_val))
print("Test:", np.bincount(y_test))
# %% [markdown]
#
# ## Define and Train Models
#
# We define the four classification models we want to compare:
#
# *  **Logistic Regression:** A linear model for binary/multinomial classification.
# *  **Decision Tree:** A non-linear model that splits data based on feature thresholds.
# *  **Gaussian Naive Bayes:** A probabilistic classifier based on Bayes' theorem with an assumption of Gaussian (normal) distribution for features.
# *  **Random Forest:** An ensemble method using multiple decision trees to improve robustness and accuracy, reducing overfitting compared to a single tree.
#
# We then train each model using the `fit` method on the *Training set* (`X_train`, `y_train`).
# Basic logging (print statements) indicates the start and end of training for each model.
#
# *   Logistic Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# *   Decision Tree: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
# *   Gaussian Naive Bayes: https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
# *   Random Forest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
#

# %%

print("\n--- Model Training ---")

# Define models
# Setting random_state for reproducibility where applicable (Decision Tree, Random Forest)
models = {
    "Logistic Regression": LogisticRegression(max_iter=200, random_state=42), # Increased max_iter for convergence
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Gaussian Naive Bayes": GaussianNB(),
    "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100) # n_estimators=100 is a common default
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
# We calculate key performance metrics:
#
# *   **Accuracy:** Overall percentage of correct predictions.
# *   **Precision:** Ability of the classifier not to label a negative sample as positive.
# *   **Recall (Sensitivity):** Ability of the classifier to find all positive samples.
# *   **F1-Score:** Weighted average of Precision and Recall. Often a good balance metric.
#
# We use 'weighted' averaging for precision, recall, and F1 because this is a multi-class problem, accounting for class imbalance if present.
#
# We also generate a Confusion Matrix for each model. This matrix visualizes the performance by showing correct and incorrect predictions for each class.
# *   Rows typically represent the true class.
# *   Columns typically represent the predicted class.
# *   Diagonal elements show correct predictions. Off-diagonal elements show errors.
#
#
# Classification Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics
# Confusion Matrix: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
# Precision/Recall/F1: https://en.wikipedia.org/wiki/Precision_and_recall

# %%
print("\n--- Model Validation on Validation Set ---")

validation_results = []
fig, axes = plt.subplots(2, 2, figsize=(12, 10)) # Create subplots for confusion matrices
axes = axes.ravel() # Flatten the axes array for easy iteration

for i, (name, model) in enumerate(trained_models.items()):
    print(f"\nValidating {name}...")

    # Make predictions on the validation set
    y_pred_val = model.predict(X_val)

    # Calculate metrics
    accuracy = accuracy_score(y_val, y_pred_val)
    # Use precision_recall_fscore_support for more control and weighted averages
    precision, recall, f1, _ = precision_recall_fscore_support(y_val, y_pred_val, average='weighted')

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Weighted Precision: {precision:.4f}")
    print(f"Weighted Recall: {recall:.4f}")
    print(f"Weighted F1-Score: {f1:.4f}")

    # Store results for comparison plot
    validation_results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-Score": f1
    })

    # Generate and plot Confusion Matrix
    cm = confusion_matrix(y_val, y_pred_val, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
    disp.plot(ax=axes[i], cmap=plt.cm.Blues)
    axes[i].set_title(f"{name}\nValidation Confusion Matrix")

plt.tight_layout()
plt.show()

print("\nValidation complete. Confusion matrices displayed.")

# Convert results to Polars DataFrame for easier handling later
results_df = pl.DataFrame(validation_results)
print("\nValidation Metrics Summary:")
print(results_df)
# %% [markdown]
#
# ## Performance Comparison Visualization
#
# To easily compare the models, we visualize their performance metrics (Accuracy, Precision, Recall, F1-Score) side-by-side using bar plots. This helps in identifying which model(s) performed best on the validation set according to different criteria.
#
# We use Polars' `melt` function to reshape the DataFrame for easier plotting with Seaborn, where each row represents a specific metric for a specific model.
#
# *   Data Visualization: https://seaborn.pydata.org/tutorial/categorical.html
#

# %%

print("\n--- Performance Comparison Visualization ---")

# Melt the DataFrame to long format suitable for seaborn barplot
results_melted_df = results_df.melt(
    id_vars="Model",
    value_vars=["Accuracy", "Precision", "Recall", "F1-Score"],
    variable_name="Metric",
    value_name="Score"
)

print("\nReshaped data for plotting:")
print(results_melted_df)

# Create the bar plot
plt.figure(figsize=(12, 7))
sns.barplot(data=results_melted_df.to_pandas(), x="Model", y="Score", hue="Metric", palette="viridis") # Convert to pandas for seaborn
plt.title("Model Performance Comparison on Validation Set")
plt.ylabel("Score")
plt.xlabel("Model")
plt.ylim(0.8, 1.0) # Adjust y-axis limits to better show differences if scores are high
plt.legend(loc='lower right')
plt.xticks(rotation=15) # Slightly rotate x-axis labels if needed
plt.show()

print("Performance comparison plot displayed.")


# %% [markdown]
#
# ## Best Model Selection and Final Test Evaluation
#
# Based on the validation results (e.g., highest F1-score or Accuracy), we select the best-performing model.
#
# We now evaluate this chosen model on the *Test Set* (`X_test`, `y_test`), which the model has NEVER seen before (neither during training nor validation). This gives the most realistic estimate of how the model would perform on new, unseen data in a real-world scenario.
# We calculate the final metrics and display the confusion matrix for the test set.
#
# *   Model Selection: https://scikit-learn.org/stable/model_selection.html
# *   Importance of Test Set: https://developers.google.com/machine-learning/crash-course/validation/check-your-intuition
#

# %%

print("\n--- Best Model Selection and Final Test Evaluation ---")

# Select the best model based on a chosen metric (e.g., F1-Score)
# We sort the results DataFrame by F1-Score in descending order and pick the top one.
best_model_row = results_df.sort("F1-Score", descending=True).row(0, named=True)
best_model_name = best_model_row['Model']
best_model = trained_models[best_model_name] # Retrieve the trained model object

print(f"Selected Best Model (based on Validation F1-Score): {best_model_name}")
print(f"Validation F1-Score of Best Model: {best_model_row['F1-Score']:.4f}")

# Evaluate the best model on the Test Set
print(f"\nEvaluating {best_model_name} on the Test Set...")
y_pred_test = best_model.predict(X_test)

# Calculate final metrics on the test set
test_accuracy = accuracy_score(y_test, y_pred_test)
test_report = classification_report(y_test, y_pred_test, target_names=target_names)
test_cm = confusion_matrix(y_test, y_pred_test, labels=best_model.classes_)

print("\n--- Final Test Set Performance ---")
print(f"Test Accuracy: {test_accuracy:.4f}")
print("\nTest Classification Report:")
print(test_report)

# Plot the confusion matrix for the test set
print("\nPlotting Test Set Confusion Matrix...")
fig, ax = plt.subplots(figsize=(6, 5))
disp = ConfusionMatrixDisplay(confusion_matrix=test_cm, display_labels=target_names)
disp.plot(ax=ax, cmap=plt.cm.Greens) # Use a different color map for distinction
ax.set_title(f"{best_model_name}\nFinal Test Set Confusion Matrix")
plt.show()

print("\nFinal evaluation complete.")

# Interpretation: The test set results represent the expected performance of your chosen
# model on completely new data. Compare these results to the validation results.
# Similar performance suggests a robust model. Significantly worse performance might
# indicate overfitting to the training/validation data or that the test set has
# different characteristics. For the raw dataset, models usually perform very well
# across all sets due to its simplicity and clear class separation.
