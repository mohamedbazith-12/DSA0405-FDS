import pandas as pd

# Load dataset
df = pd.read_csv("employee.csv")

print("Employee Dataset Summary")
print("------------------------")

# Number of rows
print("Number of Rows:", df.shape[0])

# Number of columns
print("Number of Columns:", df.shape[1])

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe(include='all'))
