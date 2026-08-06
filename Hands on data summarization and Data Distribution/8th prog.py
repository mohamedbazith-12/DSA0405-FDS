import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Titanic.csv")

# Dataset Information
print("Dataset Information")
print(df.info())

# Missing Values
print("\nMissing Values")
print(df.isnull().sum())

# Descriptive Statistics
print("\nDescriptive Statistics")
print(df.describe())

# Histograms
df.hist(figsize=(10,8))
plt.show()

# Box Plots
numeric = df.select_dtypes(include=['int64', 'float64'])

for col in numeric.columns:
    plt.boxplot(df[col].dropna())
    plt.title(col)
    plt.show()

# Detect and Remove Outliers
cleaned = df.copy()

for col in numeric.columns:

    Q1 = cleaned[col].quantile(0.25)
    Q3 = cleaned[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    cleaned = cleaned[(cleaned[col] >= lower) & (cleaned[col] <= upper)]

print("\nOriginal Shape:", df.shape)
print("Cleaned Shape:", cleaned.shape)

# Save cleaned dataset
cleaned.to_csv("Titanic_Cleaned.csv", index=False)

print("Cleaned dataset saved as Titanic_Cleaned.csv")
