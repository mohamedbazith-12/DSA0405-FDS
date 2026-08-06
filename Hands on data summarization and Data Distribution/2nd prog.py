import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

grade_counts = df["Grade"].value_counts().sort_index()

print(grade_counts)

grade_counts.plot(kind='bar')

plt.title("Frequency Distribution of Grades")
plt.xlabel("Grades")
plt.ylabel("Frequency")
plt.show()
