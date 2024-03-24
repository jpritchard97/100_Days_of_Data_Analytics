# Day 8: Feature Engineering - Creating New Features

## Task:
Create new features from existing ones in the dataset.

## Description:
Generating new features based on domain knowledge or by combining existing features to improve model performance. **Feature Engineering** is a crucial step in the machine learning pipeline where new features are created from existing ones in the dataset. This process aims to enhance model performance by providing additional information or by transforming the existing features to make them more predictive.

## Common techniques for creating new features:
- **Polynomial Features**: Transforming features by considering their polynomial combinations can sometimes capture non-linear relationships better. For instance, if you have features 'x' and 'y', you can create new features like 'x^2', 'y^2', 'xy', etc.
- **Interaction Terms**: Creating interaction terms involves multiplying or otherwise combining two or more features to capture relationships that might not be apparent when considering each feature individually. For example, in a dataset with features 'age' and 'income', creating an interaction term 'age * income' could capture the notion that the impact of age on a certain outcome might be different for different income levels.
- **Binning or Bucketing**: Continuous features can be converted into categorical features by binning or bucketing them into discrete intervals. This can help capture non-linear relationships and reduce the impact of outliers.
- **Encoding Categorical Variables**: If the dataset contains categorical variables, they can be encoded into numerical values using techniques like one-hot encoding, label encoding, or target encoding.
- **Feature Scaling**: Scaling features to a similar range can be beneficial for certain machine learning algorithms, particularly those sensitive to the scale of features, such as distance-based algorithms like k-nearest neighbors or gradient descent-based algorithms like SVMs and neural networks.
- **Time-based Features**: If the dataset involves temporal data, creating features such as day of the week, month, season, or time elapsed since a particular event can provide valuable information for prediction.
- **Handling Missing Data**: Address missing values through imputation or removal of instances or features with missing data. There are many algorithmic approaches to handling missing data.
- **Variable Encoding**: Convert categorical variables into a numerical format suitable for machine learning algorithms using methods.

## Importance
Feature engineering is both useful and necessary for the following reasons:
- Often better predictive accuracy: Feature engineering techniques such as standardization and normalization often lead to better weighting of variables which improves accuracy and sometimes leads to faster convergence.
- Better interpretability of relationships in the data: When we engineer new features and understand how they relate with our outcome of interest, that opens up our understanding of the data. If we skip the feature engineering step and use complex models (that to a large degree automate feature engineering), we may still achieve a high evaluation score, at the cost of better understanding our data and its relationship with the target variable.

# Load the Dependencies 
```python
import pandas as pd
import numpy as np

df = pd.read_csv('suicide_rates_1990-2022.csv')
df.head()
```
## Numeric aggregation
Numeric aggregation is a common feature engineering approach for longitudinal or panel data - data where subjects are repeated. In our dataset, we have categorical variables with repeated observations.

Numeric aggregation involves three parameters:

1. Categorical column
2. Numeric column(s) to be aggregated
3. Aggregation type: Mean, median, mode, standard deviation, variance, count etc.

In the following block our three parameters are:

1. 'CountryNames' - categorical column.
2. 'Population', 'GDP', 'SuicideCount' & 'GrossNationalIncome' - numeric columns to be aggregated
3. Mean, standard deviation, and count – aggregations to be used on the numeric columns

```python
4. # Calculate mean suicide count per country
suicide_per_country_mean = df.groupby('CountryName')['SuicideCount'].mean().reset_index()
suicide_per_country_mean.rename(columns={'SuicideCount': 'Suicide_per_Country_mean'}, inplace=True)

# Calculate mean GDP per country
gdp_per_country_mean = df.groupby('CountryName')['GDP'].mean().reset_index()
gdp_per_country_mean.rename(columns={'GDP': 'GDP_per_Country_mean'}, inplace=True)

# Merge the two dataframes on 'CountryName'
merged_df = pd.merge(suicide_per_country_mean, gdp_per_country_mean, on='CountryName')

# Now you have a dataframe with SuicideCount and GDP per country mean
merged_df.head(10)
```

