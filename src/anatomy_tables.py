import pandas as pd

# Load simplified dataset
df = pd.read_csv("../data/adult_simplified.csv")

# Create Group IDs
group_size = 5

df["Group_ID"] = (df.index // group_size) + 1

# Create QIT
qit = df[["Age", "Education", "Sex", "Group_ID"]]

# Create ST
st = df[["Group_ID", "Target"]]

# Save results
qit.to_csv("../results/QIT.csv", index=False)
st.to_csv("../results/ST.csv", index=False)

print("QIT and ST tables created successfully!")

print("\nQIT Preview:")
print(qit.head())

print("\nST Preview:")
print(st.head())

print("\nNumber of Records:", len(df))
print("Number of Groups:", df["Group_ID"].nunique())