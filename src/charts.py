import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/adult_simplified.csv")

income_counts = df["Target"].value_counts()

plt.figure(figsize=(6,4))
income_counts.plot(kind="bar")
plt.title("Income Distribution")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("../images/income_distribution.png")

print("Chart created successfully.")