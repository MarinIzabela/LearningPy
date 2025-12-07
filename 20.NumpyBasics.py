import numpy as np

numbers = np.array([10,20,30])
totalNumbers = np.sum(numbers)
#print(totalNumbers)


sales = np.array([
    [100,150, 200],
    [200,300,80],
    [50,70,40],
    [20,40,15]
    ]
)

value =sales[1,2]
print("Value at row 1 column 2 : ", value)

slice_parte = sales[0:3,1:3] #row 0:2 , column 1:2
print("Rows 0 to 2 , columns 1 to 2\n", slice_parte)