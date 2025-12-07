import numpy as np

data = np.loadtxt("amazon_data.csv",delimiter=",",skiprows=1, usecols=(1,2,3))# now we have only numbers

#we stores each column separatly
sales = data[:,0] #vanzarile
customers = data[:,1] #clientii
orders = data[:,2] #comenzile

total_sales = np.sum(sales)
total_customers = np.sum(customers)
total_orders = np.sum(orders)
avg_sales = np.mean(sales)
max_sales = np.max(sales)
min_sales = np.min(sales)
print(f"Min sales: {min_sales:.2f} ")
print("Max_sales: ",max_sales)
print(f"Avg sales: {avg_sales:.2f} ")

print("Total Customers : ",total_customers)
avg_customers = np.mean(customers)
max_customers = np.max(customers)
min_customers = np.min(customers)
total_orders = np.sum(orders)
avg_orders = np.mean(orders)
max_orders = np.max(orders)
print("Total Orders: " , total_orders)
print(f"Avg Orders: {avg_orders:.2f} ")
print("Max Orders: " , max_orders)
print(f"Avg Customers: {avg_customers:.2f} ")

#reshape array
data = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshaped = np.reshape(data,(3,4))
print("Reshaped Array\n ", reshaped)

more_data = np.array([
    [13,14,15,16],
    [17,18,19,20],
    [21,22,23,24]
    ]
)
print("\n")
combined_v= np.vstack((reshaped,more_data))
combined_h= np.hstack((reshaped,more_data))
print("Combined Array vertically \n ", combined_v)
print("\n")
print("Combined Array horizontally\n ", combined_h)

