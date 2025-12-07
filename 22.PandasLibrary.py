
import pandas as pd



#work with real data
## to open file like .csv, filtered , sorted and do calculation
# add also the column info, rows info, not only numbers
#it helps generate reports

#
#to select Row/column name_column = data['name'], 2 column name_column = data[['name', 'score']]
# to change something in the data .sort_values() , .groupby(), .filter(),  fillna()
# to save result we create a variable ex: clean_data = data,fillna(2)

#basic pandas function
#sales_data.csv


data = pd.read_csv("sales_data.csv")
#shows first 5 rows of data but can be defined more o few
print(data.head())
#shows the end-of the file
print("\n")
print(data.tail())
print("\n")
print(data.info())# shows how many data, what type of data and if there are missing data
print("\n")
print(data.describe())#shows details about the data like statistics mean, min, max and count
print("\n")
print(data.columns)
print("\n")
print(data.index)# show the row number
print("\n")
print(data.shape) # show how many rows and columns for eg( 10 rows, 5 columns,)
print("\n")
print(data["Price"])# shows price column
print(data[data["Price"]>100])# shows all data  with a condition
print("\n")
print(data.isnull())
print("\n")
print(data.isnull().sum()) #shows how many are null
print("\n")
data_clean = data.dropna(how="all")
print("\n")
print(data_clean)
print("\n")
data_filled = data.fillna(0)# to fill the Na data
print(data_filled)
print("\n")
sorted_data = data_filled.sort_values("Price", ascending=False)
print(sorted_data)
print("\nGrouped_data: ")
grouped_data = data.groupby("City")["Quantity"].sum()
print(grouped_data)

print("\n Renamed Data:")
data = data.rename(columns={"Price": "UnitPrice"})
print(data.head())

print("\n Adding a new column:")
data["Quantity"] = pd.to_numeric(data["Quantity"], errors="coerce")
data["UnitPrice"] = pd.to_numeric(data["UnitPrice"], errors="coerce")
data["TotalAmount"]=data["Quantity"]*data["UnitPrice"]
print(data)

print("\n Data droped")
print(data.columns)
data = data.drop("Date", axis=1) # axis = 1 coloana, axis=0 , rand
print(data)

print("\n Delete Duplicates")
data = data.drop_duplicates()
print(data)
print("\n")

data.to_csv("clean_sales_data.csv" , index=False)
print("Cleaned data saved to the new file : clean_sales_data.csv")
print("\n")