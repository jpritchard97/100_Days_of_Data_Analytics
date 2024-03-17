# Data Visualisation Report

## Introduction
This report presents the results of a univariate and bivariate analysis conducted on the Black Friday Sales dataset. The analysis aims to explore the distribution of variables within the dataset and understand the relationship between two variables.

### Dataset Information
The dataset contains information about Black Friday sales, including user demographics, product details, and purchase amounts. It consists of 550,068 entries with 12 columns.

## Uninformative Plots

This section discusses potential reasons for uninformative scatter plots and strategies to improve their quality:

- **Data Distribution**: Highly concentrated or unevenly spread data points may result in cluttered or sparse scatter plots.
- **Scale**: Inappropriate axis scales could compress or stretch data, leading to distortions.
- **Outliers**: Outliers can heavily influence scatter plot appearance, especially extreme values.
- **Missing Values**: Missing values can disrupt plot continuity and interpretation.
- **Correlation Strength**: Weak or no correlation between variables may result in random point distribution.
- **Overplotting**: Too many overlapping data points can obscure individual points and trends.

To enhance scatter plots, preprocessing, handling missing values, removing outliers, adjusting axis scales, or considering alternative visualization techniques are recommended.

## What is Bivariate Analysis?

Bivariate analysis examines the relationship between two variables, understanding how changes in one variable are associated with changes in another. Techniques include scatter plots, correlation analysis, regression, contingency tables, and categorical data visualization.

By analyzing bivariate data, researchers gain insights into relationships, patterns, outliers, and predictions.

## Bivariate Analysis

### Scatter plot of Age vs. Purchase
```python
plt.scatter(df['Age'], df['Purchase'])
plt.xlabel('Age')
plt.ylabel('Purchase')
plt.title('Age vs. Purchase')
plt.show()

# Scatter plot of Occupation vs. Purchase
plt.scatter(df['Occupation'], df['Purchase'])
plt.xlabel('Occupation')
plt.ylabel('Purchase')
plt.title('Occupation vs. Purchase')
plt.show()

# Scatter plot of Product_Category_1 vs. Purchase
plt.scatter(df['Product_Category_1'], df['Purchase'])
plt.xlabel('Product_Category_1')
plt.ylabel('Purchase')
plt.title('Product_Category_1 vs. Purchase')
plt.show()

## Conclusion
This report now incorporates explanations for uninformative plots and provides detailed descriptions of the bivariate analysis conducted on the Black Friday sales dataset.
