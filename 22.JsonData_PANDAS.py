import json
from pandas import json_normalize



#open a json file
with open("nested_order_data.json") as f:
#read and convert the json in a list of dictionary
    json_data = json.load(f)
#json_normalize convert a json in a table
#record_path =>shows the elements that will be rows in the table
#meta = fields from superior level (parent), so will not be lost
flattened_data = json_normalize(json_data, record_path="order", meta=["name", "city"])
print(flattened_data)
#after the json is flattened into a data frame we can use  the functions
#Functions : info(), describe(), columns, index, shape, isnull(), dropna(), fillna(), sort_values(),
#groupby(), rename(), drop(), duplicated(), drop_duplicated(), to_csv()