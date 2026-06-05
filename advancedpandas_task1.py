import pandas as pd

customers = pd.read_csv("customer.csv")
products = pd.read_csv("product.csv")
orders = pd.read_csv("orders.csv")

#shape
print(customers.shape)
print(products.shape)
print(orders.shape)

#columns
print(customers.columns)
print(products.columns)
print(orders.columns)

#null values
print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

#duplicat rows
print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())

# Unique Counts
print(customers.nunique())
print(products.nunique())
print(orders.nunique())

# Data Quality Summary:
# 1. Loaded all three datasets successfully.
# 2. Verified shape and column names.
# 3. Checked data types.
# 4. No missing values found.
# 5. No duplicate records found.
# 6. Calculated unique values for each column.



#--------------------
#task 2
#--------------------

# Standardize column names
customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()

# Handle missing values
customers.fillna("Unknown", inplace=True)
products.fillna("Unknown", inplace=True)
orders.fillna("Unknown", inplace=True)

# Verify cleaning
print(customers.dtypes)
print(products.dtypes)
print(orders.dtypes)

print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

# Task 2 Summary:
# 1. Standardized all column names to lowercase.
# 2. Verified that data types were already correct.
# 3. Handled possible missing values using fillna().
# 4. Confirmed that no null values remain.
# 5. The DataFrames are now ready for analysis.