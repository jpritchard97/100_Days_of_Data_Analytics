# Day 1: Data Loading and Basic Exploration

## Task: 

# Load a dataset into a Pandas DataFrame and perform basic exploration.

## Dataset: Mental Health Dataset from Kaggle

URL: https://www.kaggle.com/datasets/divaniazzahra/mental-health-dataset

## Description: 

# In this task, we will load a dataset into a Pandas DataFrame and perform basic exploration using Python.

### Steps:

# 1. Load the dataset into a Pandas DataFrame using read_csv() function.
# 2. Display the first few rows of the dataset using the head() method to understand its structure and format.
# 3. Check the data types of each column using the info() method to identify any inconsistencies or missing values.
# 4. Calculate summary statistics for numerical columns using the describe() method to gain insights into the data distribution.
# 5. Identify missing values in the dataset using methods like isna().

# Data analysis packages
import pandas as pd
import numpy as np

# Read the dataset via Pandas
df = pd.read_csv('Mental Health Dataset.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Obtain dataset information
print("\nDataset Information:")
print(df.info())

# Describe the dataset to obtain summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Identify NaN values in table format
print("\nIdentify NaN values in the dataset:")
print(df.isna())

# Count NaN values in each column
nan_values_count = df.isna().sum()

# Print the result
print("\nCount of NaN values in each column:")
print(nan_values_count)
