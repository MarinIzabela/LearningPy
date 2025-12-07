import numpy as np

class EcosystemSimulation:
    def __init__(self):
        self.population_data=None
    def simulate_growth(self):
        self.population_data=np.random.logistic(loc=50, scale=10, size=12)#loc=50=>majoritatea pop vor fi in jur de 50 animale, scale=dispersia, size = months


    def display_population(self):
        print("Simulated Monthly Population Growth:")
        months =[
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ]

        for i in range(12):
            print(f"{months[i]}:{round(self.population_data[i])} animals")



simulator = EcosystemSimulation()
simulator.simulate_growth()
simulator.display_population()

