import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset again for visualization
df = pd.read_csv("data.csv")

# Line Chart: Trends Over Time
plt.figure(figsize=(8, 5))
plt.plot(df["TimeColumn"], df["ValueColumn"], marker='o', linestyle='-')
plt.title("Trend Over Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# Bar Chart: Comparison Across Categories
plt.figure(figsize=(8, 5))
sns.barplot(x=df["CategoryColumn"], y=df["NumericalColumn"])
plt.title("Comparison Across Categories")
plt.xlabel("Category")
plt.ylabel("Value")
plt.show()

# Histogram: Distribution of Numerical Column
plt.figure(figsize=(8, 5))
plt.hist(df["NumericalColumn"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Values")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot: Relationship Between Two Columns
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["ColumnA"], y=df["ColumnB"], hue=df["CategoryColumn"])
plt.title("Scatter Plot: ColumnA vs ColumnB")
plt.xlabel("ColumnA")
plt.ylabel("ColumnB")
plt.legend(title="Category")
plt.show()
