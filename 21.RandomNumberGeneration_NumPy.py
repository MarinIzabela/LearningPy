import numpy as np


random_decimal = np.random.rand()
print("Random decimal between 0 and 1: ",random_decimal)

random_int = np.random.randint(0,11)
print("Random integer between 1,11: ",random_int)

flavors = ['chocolate', 'vanilla', 'strawberry', 'mint']
random_flavor = np.random.choice(flavors)
print("Random ice ceam flavor: ", random_flavor)

random_array = np.random.rand(5)
print("Array of 5 random decimals: ", random_array)