import pandas as pd

# Load original dataset
df = pd.read_csv("../data/adult.csv")

# Select required columns
df = df[["Age", "Education", "Sex", "Target"]]

# Remove missing values
df = df.dropna()

# Save simplified dataset
df.to_csv("../data/adult_simplified.csv", index=False)

print("Dataset prepared successfully!")
print(df.head())
print("\nDataset Shape:")
print(df.shape)