# Data Preprocessing - Encoding Categorical Variables

## Task:
Encode categorical variables into numerical format for machine learning models.

## Description:
Data preprocessing is a crucial step in preparing data for machine learning models. Encoding categorical variables is one such preprocessing step, which involves converting categorical data into a numerical format that can be utilized by machine learning algorithms. This markdown file demonstrates two common techniques for encoding categorical variables: Label Encoding and One-Hot Encoding.

## What are Encoding Categorical Variables?

In the context of data preprocessing, encoding categorical variables refers to converting categorical data into a numerical format that can be utilized by machine learning algorithms. Two popular methods for encoding categorical variables are Label Encoding and One-Hot Encoding.

### Label Encoding:

Label encoding involves assigning a unique integer to each category in a categorical variable. It is suitable for ordinal categorical variables where there exists an inherent order among categories.

```python
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load dataset
suicide_data_le = pd.read_csv("suicide_rates_1990-2022.csv")

# Assuming 'CountryName' is the column with country names
country_labels = suicide_data_le['CountryName']

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform country labels
encoded_countries = label_encoder.fit_transform(country_labels)

# Replace the original 'CountryName' column with the encoded values
suicide_data_le['CountryName'] = encoded_countries
```

## Explanation:

- from sklearn.preprocessing import LabelEncoder: Importing the LabelEncoder class from the sklearn library, which is used for label encoding.
- suicide_data_le = pd.read_csv("suicide_rates_1990-2022.csv"): Loading the dataset containing suicide rates.
- country_labels = suicide_data_le['CountryName']: Extracting the 'CountryName' column, which contains categorical data.
- label_encoder = LabelEncoder(): Initializing a LabelEncoder object.
- encoded_countries = label_encoder.fit_transform(country_labels): Fitting and transforming the 'CountryName' labels into encoded numerical values.
- suicide_data_le['CountryName'] = encoded_countries: Replacing the original 'CountryName' column with the encoded numerical values.

```python
import pandas as pd

# Load dataset
suicide_data = pd.read_csv("suicide_rates_1990-2022.csv")

# Assuming 'CountryName' is the column with country names
country_dummies = pd.get_dummies(suicide_data['CountryName'], prefix='CountryName')

# Concatenate the one-hot encoded columns with the original dataframe
suicide_data = pd.concat([suicide_data, country_dummies], axis=1)

# Drop the original 'CountryName' column if needed
suicide_data.drop('CountryName', axis=1, inplace=True)
```
## Explanation:

- import pandas as pd: Importing the pandas library for data manipulation.
- suicide_data = pd.read_csv("suicide_rates_1990-2022.csv"): Loading the dataset containing suicide rates.
- country_dummies = pd.get_dummies(suicide_data['CountryName'], prefix='CountryName'): Generating one-hot encoded columns for each category in the 'CountryName' column.
- suicide_data = pd.concat([suicide_data, country_dummies], axis=1): Concatenating the one-hot encoded columns with the original dataframe.
- suicide_data.drop('CountryName', axis=1, inplace=True): Dropping the original 'CountryName' column if needed.

These techniques demonstrate how to preprocess categorical variables for machine learning tasks, making the data suitable for use in machine learning algorithms.

