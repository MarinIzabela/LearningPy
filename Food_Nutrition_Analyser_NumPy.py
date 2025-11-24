import numpy as np

class McDonaldNutritionAnalyser:
    def __init__(self):
        self.food_items = np.array(['Big Mac', 'Fries','McChicken','Coke'])
        self.nutrition_data = np.array([
            [550,25,30],
            [320,4,15],
            [400,14,21],
            [150,0,0]
        ])

    def show_all_items(self):
        print("McDonald Items and their Nutrition(Calorie, Protein, Fat):")
        for i in range(len(self.food_items)):
             print(self.food_items[i],":",self.nutrition_data[i])


    def get_total_nutrition(self):
        total=self.nutrition_data.sum(axis=0)
        print("\nTotal Nutrition for all items:")
        print("Calories:",total[0])
        print("Protein:",total[1],"gr")
        print("Fats:",total[2],"gr")


    def reshape_nutrition(self):
        reshaped =self.nutrition_data.reshape(2,6)
        print("\nReshaped Nutrition , 2 rows and 6 columns :")
        print(reshaped)

    def add_new_food(self, name, calories, protein, fats):
        self.food_items= np.append(self.food_items,name)
        new_data = np.array([[calories,protein,fats]])
        self.nutrition_data = np.vstack((self.nutrition_data,new_data))
        print("\n" , name," added succesfully  :")



analyzer = McDonaldNutritionAnalyser()
analyzer.show_all_items()
analyzer.get_total_nutrition()
analyzer.reshape_nutrition()
analyzer.add_new_food("McChicken",350,50,5)
analyzer.show_all_items()
analyzer.get_total_nutrition()