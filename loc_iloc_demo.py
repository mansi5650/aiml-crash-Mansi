import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

print("Original DataFrame:")
print(df)

# Set Name as index for .loc example
df_indexed = df.set_index("Name")

# ---------------------------
# .loc Example (Label-Based)
# ---------------------------
print("\nUsing .loc:")
print(df_indexed.loc["Priya", ["Course", "Marks"]])

# ----------------------------
# .iloc Example (Position-Based)
# ----------------------------
print("\nUsing .iloc:")
print(df.iloc[2, [2, 3]])