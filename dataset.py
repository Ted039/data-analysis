import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display first few rows
print("Dataset Preview:\n", df.head())

# Explore structure
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Clean dataset (Fill missing values or drop rows)
df.dropna(inplace=True)  # OR df.fillna(df.mean(), inplace=True)

# Compute basic statistics
print("\nBasic Statistics:\n", df.describe())

# Perform groupings and compute mean
grouped_df = df.groupby("CategoryColumn").mean()
print("\nGrouped Data:\n", grouped_df)
