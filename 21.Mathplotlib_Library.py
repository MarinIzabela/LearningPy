import matplotlib.pyplot as plt


years = [2020,2021,2022,2023,2024,2025]
new_customers = [15000, 10000,  3000, 8000, 5000, 4000]

plt.plot(years,new_customers)
plt.xlabel("Years")
plt.ylabel("Customers")
plt.title("Yearly Growth of a new customers")
plt.show()
plt.show()