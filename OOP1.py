class Patient:
    def __init__(self,name, age, disease):
        self.name = name
        self.age = age
        self.__disease = disease
    def show_basic_info(self):
        print(f"Patient name:{self.name}, Age:{self.age}")
    def show_full_info(self, is_doctor):
        if is_doctor:
            print(f"Patient name:{self.name}, Age:{self.age} , Disease: {self.__disease}")
        else:
            print("Acces Denied:You are not authorize to view medical details")

name = input("Enter patient name: ")
age = int(input("Enter patient age:"))
disease = input("Enter patient's disease:")

patient1 = Patient(name, age, disease)
patient1.show_basic_info()

user_role = input("\n Are you a doctor?(yes/no)").strip().lower()
is_doctor = user_role == "yes"
patient1.show_full_info(is_doctor)

# trying to access private data directly(this will not work)
print(patient1.__disease)