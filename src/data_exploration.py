import pandas as pd

df = pd.read_csv("../data/adult.csv")

print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)