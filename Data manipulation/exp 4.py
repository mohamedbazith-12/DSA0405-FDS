import pandas as pd

# Sample data
data = {
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 90000, 110000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}

df = pd.DataFrame(data)

# Summary of numeric columns
print("--- Numeric Summary ---")
print(df.describe())

# Summary of categorical columns
print("\n--- Categorical Summary ---")
print(df.describe(include='object'))
