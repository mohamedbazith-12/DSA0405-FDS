import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("house_prices.csv")

plt.hist(df["Price"], bins=20)

plt.title("Histogram of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

print("Observe the histogram:")
print("- Bell-shaped → Normally Distributed")
print("- Left/Right Tail → Skewed Distribution")
