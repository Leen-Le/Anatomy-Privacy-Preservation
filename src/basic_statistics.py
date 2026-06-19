import pandas as pd

df = pd.read_csv("../data/adult_simplified.csv")

print("Total Records:", len(df))

print("\nIncome Distribution:")
print(df["Target"].value_counts())

print("\nGender Distribution:")
print(df["Sex"].value_counts())

print("\nEducation Distribution:")
print(df["Education"].value_counts().head(10))