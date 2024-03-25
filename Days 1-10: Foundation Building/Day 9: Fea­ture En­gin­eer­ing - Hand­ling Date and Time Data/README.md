# Day 9: Feature Engineering - Handling Date and Time Data

## Task
- The task involves extracting relevant information from date and time columns.

## Description
- In this task, I leverage Pandas' date-time functionalities to extract features such as the day of the week, month, or year from date-time columns.

## Loading the Dependencies
To accomplish this task, I utilize the `pd.to_datetime()` function from the Pandas library.

### Method
```python

# Convert the 'Date' column to datetime format, handling mixed formats
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the updated DataFrame
print(df.head())
```

Upon execution, this code snippet converts the 'Date' column in the DataFrame (`df`) to datetime format, while handling any mixed formats that might exist within the data. Here's a breakdown of what each part of the code does:

- `pd.to_datetime(df['Date'], errors='coerce')`: This line converts the 'Date' column to datetime format. The `errors='coerce'` parameter handles any errors encountered during conversion by converting problematic entries to NaT (Not a Time), effectively ignoring them.

- `print(df.head())`: This line prints the first few rows of the updated DataFrame, allowing us to inspect the changes made.
