import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

plt.boxplot(df["Salary"])

plt.title("Box Plot of Salary")
plt.ylabel("Salary")
plt.show()

print("Points outside whiskers indicate outliers.")
