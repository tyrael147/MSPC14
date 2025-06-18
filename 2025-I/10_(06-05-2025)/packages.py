#!/usr/bin/env python
# coding: utf-8
# %%

# %% [markdown]
# # Creating Installable Python Packages
#
# This notebook will guide you through the process of creating a basic installable Python package.
# Installable packages allow you to easily share and reuse your code across different projects and with others.
# We'll be using `pyproject.toml` which is the modern standard for Python packaging configuration.

# %% [markdown]
# ## 1. Project Structure
#
# A typical Python package has a specific directory structure. Let's imagine we're creating a package named `mypackage`.
#
# ```
# my_project_directory/
# ├── pyproject.toml         # Configuration file (THIS IS KEY!)
# ├── README.md              # Description of your package
# ├── src/                   # Optional: source layout (recommended)
# │   └── mypackage/         # Your actual package code
# │       ├── __init__.py    # Makes the directory a package
# │       └── module1.py     # A module within your package
# │       └── ...            # Other modules/subpackages
# └── ...                    # Other files like tests/, docs/, examples/
# ```
#
# For simplicity in this guide, we might omit `src/` and place `mypackage` directly in the root, but using `src/` is best practice for larger projects to avoid namespace conflicts.
#
# Let's create a minimal structure.

# %% [markdown]
# ### Create Example Files
#
# You would typically create these files in your file system. For this notebook, we'll simulate their content.
#
# **`mypackage/__init__.py`**:
# This file can be empty, or it can define what gets imported when someone does `from mypackage import ...` or `import mypackage`. It also signals to Python that the `mypackage` directory should be treated as a package.

# %%
# Content for: mypackage/__init__.py
# This makes functions/classes from module1 directly available
# e.g., from mypackage import greet_user

# __all__ = ["greet_user"] # Optional: defines what 'from mypackage import *' imports
# from .module1 import greet_user

# print("mypackage loaded!") # For demonstration

# %% [markdown]
# **`mypackage/module1.py`**:
# This is where your actual Python code lives.

# %%
# Content for: mypackage/module1.py

# def greet_user(name="World"):
#     """Greets the user."""
#     return f"Hello, {name}! Welcome to mypackage."

# def add_numbers(a, b):
#     """Adds two numbers."""
#     return a + b

# %% [markdown]
# ## 2. The `pyproject.toml` Configuration File
#
# This is the heart of modern Python packaging. It tells build tools (like `pip` and `build`) how to build your package and what its metadata is.
#
# It's written in TOML (Tom's Obvious, Minimal Language).
#
# There are two main sections we'll focus on:
# 1.  `[build-system]`: Specifies the build backend (e.g., setuptools, flit, poetry, hatchling).
# 2.  `[project]`: Contains metadata about your package (name, version, dependencies, etc.).

# %% [markdown]
# ### `[build-system]` Section
#
# This section is **REQUIRED**. It tells `pip` how to build your package.
#
# *   `requires`: A list of packages needed to *build* your package.
# *   `build-backend`: The Python object that frontends will use to perform the build.
# *   `backend-path`: (Optional) A list of directories to search for the backend. Usually not needed if the backend is installed from PyPI.
#
# For `setuptools` (a very common backend):

# %%
# Content for: pyproject.toml (partial - build-system)

# [build-system]
# requires = ["setuptools>=61.0"] # Required: Specifies setuptools version
# build-backend = "setuptools.build_meta" # Required: The build backend function
# backend-path = ["."] # Optional, often not needed if setuptools is in `requires`

# %% [markdown]
# ### `[project]` Section
#
# This section contains metadata about your package.
#
# **REQUIRED arguments in `[project]`:**
#
# *   `name`: (String) The distribution name of your package (e.g., `my-package`). This is what you type when you `pip install my-package`.
# *   `version`: (String) The version number of your package (e.g., `"0.1.0"`). PEP 440 compliant.
#
# **STRONGLY RECOMMENDED (often practically required for sharing):**
#
# *   `description`: (String) A short, one-sentence summary of the package.
# *   `readme`: (String or Table) Path to a file containing the long description (e.g., `"README.md"`). The table form allows specifying content-type.
# *   `authors`: (Array of Tables) e.g., `[{name = "Your Name", email = "you@example.com"}]`
# *   `license`: (Table or String) e.g., `{file = "LICENSE"}` or `{text = "MIT License"}`.
# *   `requires-python`: (String) The Python versions your package supports (e.g., `"> C\Users\joshu\Documents\projects\learning-python-packaging\my_project_directory\src\mypackage
# src\mypackage\module1.py
# src\mypackage\__init__.py
# my_project_directory\pyproject.toml
# (my_project_directory)
# (my_project_directory\src)
# (my_project_directory\src\mypackage)
# python -m build
# pip install .
# python
# from mypackage import greet_user, add_numbers
# print(greet_user("Student"))
# print(add_numbers(5, 3))
# exit()
# pip uninstall mypackage
# pip install -e .
# (Modify module1.py - e.g., change the greeting message)
# python
# from mypackage import greet_user
# print(greet_user("Developer")) # Should show the updated message
# exit()
# pip uninstall mypackage
# ```
#
# You would then run these commands in your terminal, in the `my_project_directory`.

# %% [markdown]
# ## 5. Installing and Using the Package
#
# Once built, you can install your package.
#
# **Install from local build artifacts (wheel file):**
# ```bash
# # Navigate to your project's root directory (e.g., my_project_directory)
# pip install dist/mypackage-0.1.0-py3-none-any.whl
# ```
# (The exact filename of the `.whl` file will depend on your package name and version.)
#
# **Install directly from source (useful for development):**
# ```bash
# # Navigate to your project's root directory
# pip install .
# ```
#
# **Editable install (highly recommended for development):**
# This installs the package in a way that changes to your source code are immediately reflected without needing to reinstall.
# ```bash
# # Navigate to your project's root directory
# pip install -e .
# ```
#
# ### Testing the Installation
#
# After installing, you can try importing and using it in a Python interpreter:
#
# ```python
# >>> from mypackage import greet_user, add_numbers
# >>> print(greet_user("Student"))
# Hello, Student! Welcome to mypackage. This is version 0.1.0.
# >>> print(add_numbers(10, 5))
# 15
# >>> import mypackage
# mypackage loaded!
# >>> mypackage.some_variable
# 42
# ```

# %% [markdown]
# ## 6. Summary of Required Arguments
#
# To recap, the **absolutely required** arguments in `pyproject.toml` for a build system like `setuptools` are:
#
# 1.  In `[build-system]`:
#     *   `requires` (e.g., `["setuptools>=61.0"]`)
#     *   `build-backend` (e.g., `"setuptools.build_meta"`)
#
# 2.  In `[project]`:
#     *   `name` (e.g., `"my-package"`)
#     *   `version` (e.g., `"0.1.0"`)
#
# While other fields like `description`, `readme`, `authors`, `license`, and `dependencies` are not strictly required by the file format specification for a local build, they are essential for creating a useful, shareable, and publishable package.

# %% [markdown]
# ## Next Steps
#
# *   Adding dependencies to other packages.
# *   Including non-Python data files.
# *   Adding entry points (scripts).
# *   Publishing your package to PyPI (Python Package Index).
# *   More complex project structures and build configurations.
#
# This provides a basic foundation. Modern Python packaging is powerful and flexible!
