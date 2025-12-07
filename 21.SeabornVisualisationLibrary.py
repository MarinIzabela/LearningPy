
import seaborn as sns
import matplotlib.pyplot as plt


#bar plots , line plots, scatter plots, heatmap
#Seaborn is built on top of Matplotlib

months = ["January", "February", "March", "April", "May",]
sales = [25000,30000,28000,35000,40000]
sns.barplot(x=months, y=sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales by Month")
plt.show()