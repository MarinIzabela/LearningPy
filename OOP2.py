class Pilot:
    #constructor
    def __init__(self, salary):
        self._salary = salary
    #getter
    @property
    def salary(self):
     return self._salary

    # setter
    @salary.setter
    def salary(self, new_salary):
        if new_salary>=100000:
            self._salary=new_salary
        else:
            raise ValueError("Salary must be greater than $100,0000 ")


pilot1 = Pilot(120000)
print(pilot1.salary)
pilot1.salary = 130000
print(pilot1.salary)