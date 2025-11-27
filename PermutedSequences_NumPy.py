
import numpy as np



#use to display the same products on site in a fresh and random order every time
# every product has a correct share , of being first product shown
products = ["Headphones" , "Tailphones", "Laptops", "Batteries"]

shuffled_product = np.random.permutation(products)

print("Product shown to customers:", shuffled_product)
