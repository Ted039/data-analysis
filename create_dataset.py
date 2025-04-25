import pandas as pd

# Sample data
data = {
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
    "Sales": [500, 300, 700],
    "Category": ["Electronics", "Clothing", "Groceries"],
    "Quantity": [10, 15, 20]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)

print("CSV file created successfully!")
