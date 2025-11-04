
class Employee:
    def __init__(self, name, employee_id, salary):
        self._name = name
        self._employee_id = employee_id
        self._salary = salary

    def show_details(self):
            print("Name ->",self._name)
            print("ID->",self._employee_id)
            print("Salary ->",self._salary)

class DeliveryDriver(Employee):
    def __init__(self, name, employee_id, salary, truck_number):
        super().__init__( name, employee_id, salary)
        self._truck_number = truck_number

    def show_details(self):
        super().show_details()
        print(f"Truck number -> {self._truck_number}")

class warehouseWorker(Employee):
    def __init__(self, name, employee_id, salary, shift):
        super().__init__(name, employee_id, salary)
        self._shift = shift

    def show_details(self):
        super().show_details()
        print(f"Shift -> {self._shift}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary,team_size):
        super().__init__(name, employee_id, salary)
        self._team_size = team_size

    def show_details(self):
         super().show_details()
         f"Team size -> {self._team_size}"




driver1 = DeliveryDriver("Ion", 1, 100, "Truck-10")
worker1 = warehouseWorker("Ionela", 2, 100, "Night")
manager1 = Manager(name="Iza", employee_id=3, salary=10000, team_size=10)

manager1.show_details()
print()
worker1.show_details()
print()
driver1.show_details()
print()