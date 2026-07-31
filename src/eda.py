import pandas as pd

# Load dataset
df = pd.read_csv("dataset/phishing.csv")

# Show first 5 rows
print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

# Shape of dataset
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())