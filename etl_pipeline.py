import pandas as pd

# Sample source data
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "salary": [50000, 60000, 70000]
}

# Extract
df = pd.DataFrame(data)

# Transform
df["salary"] = df["salary"] * 1.10

# Load
df.to_csv("processed_data.csv", index=False)

print("ETL pipeline completed successfully!")
print(df)
