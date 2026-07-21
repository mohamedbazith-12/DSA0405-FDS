import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 92, 78, 95, 88, 72, 91]
}

df = pd.DataFrame(data)

# Top 5 rows
print("Top 5 Rows:")
print(df.head())

# Top 2 rows
print("\nTop 2 Rows:")
print(df.head(2))

# Bottom 3 rows
print("\nBottom 3 Rows:")
print(df.tail(3))
