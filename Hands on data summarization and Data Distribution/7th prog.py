import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

cleaned = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

# Histogram Before
plt.hist(df["Sales"], bins=15)
plt.title("Histogram Before Removing Outliers")
plt.show()

# Histogram After
plt.hist(cleaned["Sales"], bins=15)
plt.title("Histogram After Removing Outliers")
plt.show()

# Box Plot Before
plt.boxplot(df["Sales"])
plt.title("Box Plot Before Removing Outliers")
plt.show()

# Box Plot After
plt.boxplot(cleaned["Sales"])
plt.title("Box Plot After Removing Outliers")
plt.show()
