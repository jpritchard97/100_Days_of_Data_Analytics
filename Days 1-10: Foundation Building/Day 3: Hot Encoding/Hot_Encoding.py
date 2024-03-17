import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Sample DataFrame with categorical variables
data = {'Colour': ['Red', 'Blue', 'Green', 'Red', 'Green'],
        'Size': ['Small', 'Large', 'Medium', 'Medium', 'Small']}
df = pd.DataFrame(data)

# One-Hot Encoding
one_hot_encoder = OneHotEncoder(sparse=False)
one_hot_encoded = one_hot_encoder.fit_transform(df[['Colour', 'Size']])
one_hot_df = pd.DataFrame(one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(['Colour', 'Size']))
print("One-Hot Encoded DataFrame:")
print(one_hot_df)

# Label Encoding
label_encoder = LabelEncoder()
label_encoded = df.apply(label_encoder.fit_transform)
print("\nLabel Encoded DataFrame:")
print(label_encoded)
