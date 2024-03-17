# Data Visualisation Report

## Introduction
This report presents the results of a univariate analysis conducted on the Black Friday Sales dataset. The analysis aims to explore the distribution of variables within the dataset and gain insights into purchasing behavior.

### Dataset Information
The dataset contains information about Black Friday sales, including user demographics, product details, and purchase amounts. It consists of 550,068 entries with 12 columns.

## Data Preprocessing
First, we checked basic statistics and identified missing values in the dataset. The summary statistics provided an overview of numerical variables, including counts, means, and quartiles. Missing values were found in the 'Product_Category_2' and 'Product_Category_3' columns.

### Summary Statistics
The summary statistics revealed:
- User_ID and Occupation are numerical variables.
- Marital_Status and Product_Category_1 are categorical variables.
- 'Product_Category_2' and 'Product_Category_3' have missing values.

### Missing Values
The count of NaN values in each column showed that 'Product_Category_2' had 173,638 missing values, and 'Product_Category_3' had 383,247 missing values.

To address missing values, we dropped columns containing NaN values and stored the result in a new DataFrame called `df_cleaned`. This ensured that the analysis could proceed with complete data.

## Exploratory Data Analysis (EDA)
### Age Distribution
The histogram visualisation of the 'Age' variable showed the distribution of age groups among Black Friday shoppers. The analysis revealed that individuals between the ages of 26-35 made up the highest frequencies of Black Friday purchases, while those aged 0-17 made up the lowest frequency.

### Marital Status Distribution
The bar plot visualisation of the 'Marital_Status' variable displayed the distribution of marital status among shoppers. The analysis showed that the majority of Black Friday shoppers were single, with a higher frequency compared to married individuals.

## Conclusion
The univariate analysis provided valuable insights into the Black Friday sales dataset. It revealed patterns in age groups and marital status, shedding light on the demographics of shoppers and their purchasing behavior.

Further analysis, including bivariate and multivariate analyses, could provide deeper insights into the relationships between variables and facilitate more targeted marketing strategies for Black Friday sales.

