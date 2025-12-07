import pandas as pd

data = pd.read_csv("sales_data1.csv")
print("Original Data")
print(data.head())

print("\n Missing Values in each column")
print(data.isnull().sum())
print(data.isnull().sum())
data = data.fillna(0)
data= data.drop_duplicates()

data.columns = data.columns.str.strip().str.lower()
print("Cleaned Data has been saved in clean_sales_data1.csv")
data.to_csv("clean_sales_data1.csv", index=False)

print(data.head())