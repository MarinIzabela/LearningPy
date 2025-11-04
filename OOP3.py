class Recipe:
    def __init__(self, name):
        self._name = name
        self._ingredients = {}
    @property
    def ingredient(self):
        return self._ingredients

    @ingredient.setter
    def ingredient(self, ingredient):
        self._ingredients = ingredient

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def add_ingredient(self, name, quantity):
        if quantity > 0:
            self._ingredients[name] = quantity
        else:
            print("Ingredient quantity cannot be zero")

    def sumary(self):
        print(f"Recepe:{self._name}")
        for name, quantity in self._ingredients.items():
            print(f" - {name}: {quantity}")


r = Recipe("Recipe")
r.name = "Pancake"
r.add_ingredient("Flour", 100)
r.add_ingredient("Milk", 250)
r.add_ingredient("Egg", 5)
r.sumary()
print(r.name);