# Single Inheritance, Multiple Inheritance

class Vehicle:
   def info(self):
       return "This is a Vehicle"

class Car(Vehicle):
    def type(self):
        return " This is a Car"

class Engine :
    def engine_info(self):
        return "This car has an Engine"

class Electric:
    def battery_info(self):
        return "This car runs on a Battery"

class ElectricCar(Engine, Electric):
    # we do not want to add any new functions or code, but we still need the class to exists
    # Phython does not alowed an empty class and we use this word to have acces to inheritance
    pass

# Multi level inheritance
class Animal:
    def species(self):
        return "This is a Animal"

class Mammal(Animal):
    def mamal_info(self):
        return "This is a Mammal"

class Dog(Mammal):
    def sound(self):
        return "Dog Bark"
# Hierarchical inheritance
class Phone:
    def brand(self):
        return "This is a Phone"

class Smartphone(Phone):
    def type(self):
        return "This is a Smartphone"

class Landline(Phone):
    def type(self):
        return "This is a Landline phone"


# Hybrid Inheritance
class Employee:
    def details(self):
        return "This is a Employee"
class Manager(Employee):
    def role(self):
        return "Manages the teams"
class Engineer(Employee):
    def role(self):
        return "Develops the product"

class TechLead(Manager, Engineer):
    def lead_info(self):
        return "Leads both Managers and Engineers"



car = Car()
print(car.type())  # "This is a Car"
print(car.info())  # from Vehicle

electric_Car = ElectricCar()

print(electric_Car.engine_info()) # from Vehicle
print(electric_Car.battery_info()) # from Electric

dog = Dog()
print(dog.species()) # from Animal
print(dog.mamal_info()) # from Mammal
print(dog.sound()) # from Dog

smartphone = Smartphone()
landline = Landline()
print(smartphone.type())
print(smartphone.brand())

tech_lead = TechLead()
print(tech_lead.role())  # Manager.role() e ales prin MRO
print(tech_lead.details()) # from Employee
print(tech_lead.lead_info())   # from TechLead
