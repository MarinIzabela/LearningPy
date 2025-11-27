import numpy as np

class EquipmentFailurePredictor:
    def __init__(self):
        self.failure_data = None

    def get_input(self):
        self.cycles = int(input("Enter number of test cycles per machine: "))
        self.probability = float(input("Enter probability of failure: ex:0.2 for 20%"))
        self.machine = int(input("Enter number of machines to simulate: "))

    def simulate_failure(self):
        self.failure_data = np.random.binomial(n=self.cycles, p=self.probability, size=self.machine)

    def show_result(self):
        print("\nPredicted Equipment Failure:")
        machine_number=1

        for failures in self.failure_data:
            print("Machine ," , machine_number , ": " , failures , f"failure out of {self.cycles} cycles")
            machine_number +=1




predictor = EquipmentFailurePredictor()
predictor.get_input()
predictor.simulate_failure()
predictor.show_result()


