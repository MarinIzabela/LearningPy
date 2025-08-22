#personal budget calculation
#Step 1 : get income for the user

income = int(input("Care este venitul lunar ? "))

#Step 2 Get expenses from the user
rent = int(input("Cat este chiria lunara ? "))
groceries = int(input("Cat cheltui pe mancare ? "))
transport= int(input("Cat cheltui pe transport ? "))
utilities = int(input("Cat cheltui pe utilitati? "))
other_expenses = int(input("Alte cheltuieli: ? "))


#Step 3 : Calculate the total expenses
total_expenses = rent+groceries+transport+utilities+other_expenses
print(f"Cheltuielile totale sunt de : {total_expenses} lei")

#Step 4 Calculate the remaining budget

remaining_budget = income-total_expenses
print(f"Bugetul ramas este : {remaining_budget} lei. ")