import array
import copy

# user_input = input("Introduceti numele si prenumele : ")
# firstname =user_input[0:user_input.find(" ")].capitalize()
# print(firstname)
# lastname = user_input[user_input.find(" ")+1:].capitalize()
# print(lastname)
# print(f" Hello, {firstname} {lastname}! Welcome!")


# user_input = input("Introduceti numele si prenumele : ")
# firstname, lastname = user_input.split(" ")
#
# print(f"Hello, {firstname.capitalize()} {lastname.capitalize()}! Welcome!")

# hour = int(input("Introdu ora : "))
# minute =int (input("introdu minutul:"))
# print(f"este ora {hour:02d} :{minute:02d}


# numar=float(input("Introdu un numar cu zecimale: "))
# print(f"The number rounded to 2 decimals is : {numar:.2f}")


# name = "Izabela"
# quantity = 2
# price= 200.00
#
# total_cost = quantity*price
# print(f"Thank you {name} for the order, the total cost is {total_cost:.2f} euro for {quantity} pieces. ")

# hour = 1
# if 6 <= hour <= 12:
#     greeting = "Good Morning!"
# elif hour > 12 and hour <= 17:
#     greeting="Good afternoon!"
# elif hour > 17 and hour <= 23:
#     greeting = "Good night"
# else:
#     greeting = "Go to sleep!"
#
#
# print(f" Hour:  {hour}")
# print("Greeting: " ,greeting)


# for id in range(1001, 1011):
#     if id % 2 == 0:
#         print(f"ID {id} is VIP ! ")
#     elif id == 1005:
#         continue
#     else:
#         print(f"ID {id} is STANDARD ! ")
#
#     if id==1009:
#         break

# fruits = ["mere", " pere", "banane"]
# print(fruits)
# fruits.append("mango")
# print(fruits)
# fruits.remove("banane")
# print(fruits)
# fruits.insert(2,"prune")
# print(fruits)


# numbers = [10,20,30,40,50,60,70,80,90,100]
# print(numbers[2:6])
#
# grocery_list = ["lapte", "paine", "oua", "branza", "sunca", "iaurt"]
#
# for item in grocery_list:
#     print("->" + item)

# names = ["Izabela", "Elena", "Ana", "Maria", "Roxana", "Laur"]
#
# names.sort()
#
# print(names)
#
# names.reverse()
#
# print(names)

# students = [
#     ["Ion", 16, [85,75,95]],
#     ["Maria", 16, [85,65,55]],
#     ["Ioana", 16, [95,92,98]],
# ]
#
# print("Students records: ")
# for student in students:
#     name= student[0]
#     age = student[1]
#     marks = student[2]
#     print(f"Name: {name}, Age: {age}, Marks: {marks}")


# original_list = [1,2,3,4,5]
# deep_copied_list = copy.deepcopy(original_list)

# airplanes=(
#     ("BA117", "approaching"),
#     ("LH400 ", "approaching"),
#     ("EK901 ", "delayed"),
#     ("AA390  ", "emergency")
#
# )
#
# total_aproacing = 0
#
# for plain, status in airplanes:
#     if status == "delayed":
#         print(f"Warning: {plain} is delayed!")
#     elif status == "emergency":
#         print(f"Critical Alert! {plain} has an emergency. Halting checks.")
#         break
#     elif status == "approaching":
#         print(f"Plane {plain} is approaching. Prepare clearance")
#         total_aproacing+=1
#     elif status == "landed":
#         print("Plain already landed")
#         continue
#
#
# print("Total approaching plaines:", total_aproacing)


#
# companies = {"Apple", "Microsoft" , "Google" , "Google"}
# companies.add("Amazon")
# companies.remove("Microsoft")
# print(companies)


# Frozen sets

# fast_food_brands = frozenset({"McDonald's", "Burger King", " KFC", " Subway", "Wendy's"})
# # fast_food_brands.add("Domino's")
# print(fast_food_brands)

#Subset and Superset
# all_restaurants = {"Olive Garden", " Cheesecake Factory", " Texas RoadHouse", " Chipotle", "RedLobster"}
# fine_dinning_restaurants = {"Olive Garden", "RedLobster"}
# print(fine_dinning_restaurants.issubset(all_restaurants))
# print(all_restaurants.issuperset(fine_dinning_restaurants))

# Python_beginners_course = {"Olivia", "Liam", "Noah", "Emma"}
# Python_Projcts_Course = {"Olivia", "Liam", "Sophia", "Ava"}
#
# Enrolled_in_both_courses = Python_beginners_course.intersection(Python_Projcts_Course)
# print(f"Enrolled in both courses: {Enrolled_in_both_courses}")
# difference = Python_beginners_course.difference(Python_Projcts_Course)
# print(f"Only in Beginners course: {difference}")
#
#
# difference2 = Python_Projcts_Course.difference(Python_beginners_course)
# print(f"Only in Projects course: {difference2}")
# total_Unique_Students = Python_beginners_course.union(Python_Projcts_Course)
# print(f"Total unique students:{total_Unique_Students} ")


# current_stock = {"P101", "P102", "P103", "P104"}
# print(current_stock)
# new_arrivals = {"P103", "P104", "P105", "P106"}
#
# true_new = new_arrivals.difference(current_stock)
# print(f"New Arrivals: {true_new}")
#
# updated_set=current_stock.union(new_arrivals)
# print(f"Updated stock : {updated_set}")
#
# if new_arrivals.issubset(updated_set):
#     print("All new arrivals are now in stock")
#
# discontinued = frozenset({"P101", "P102"})
# print(f"Discontinued: {discontinued}")
# discontinued = frozenset({"P101", "P102"})
# print(f"Discontinued: {discontinued}")



# amazon_inventory = {
#     "Electronics":{
#         "Mobile" :{"Price" : 5000, "Stock":30, "Rating":4.5},
#         "Laptop":{"Price":2000, "Stock":15, "Rating":4.5}
#     },
#     "Clothing":{
#         "Shirt":{"Price":5, "Stock":50, "Size":["S","M","L"]},
#         "Jeans":{"Price":6, "Stock":40, "Size":["S","M","L"]}
#     },
#     "Books":{
#         "Novel":{"Price":1, "Stock":100, "Author":"Ion Creanga"},
#         "TextBook":{"Price":7, "Stock":100, "Author":"Mihai Eminescu"}
#     }
#:
#
# }
#
# print(amazon_inventory)
# print("Novel Price: ", amazon_inventory["Books"]["Novel"]["Price"])
# amazon_inventory["Books"]["Novel"]["Price"]-=0.5
# print("Novel Price: ", amazon_inventory["Books"]["Novel"]["Price"])
# amazon_inventory["Clothing"]["Dress"]={"Price":20, "Stock":20, "Size":["S","M","L","XL","XXL"]}
#
# print("Clothing Price: ", amazon_inventory["Clothing"]["Dress"]["Price"])


# inventory = {
#     "Tools": {1: "Working", 2: "Faulty", 3: "Working"},
#     "Cable": {1: "Faulty", 2: "Faulty", 3: "Faulty"},
#     "Sensors": {1: "Faulty", 2: "Working", 3: "Working"}
# }
#
#
# def category_report(inv):
#     print("")
#     for category, components in inventory.items():
#         working_count = sum(1 for status in components.values() if status == "Working")
#         faulty_count = sum(1 for status in components.values() if status == "Faulty")
#         if working_count == 0:
#             print(f"{category}:Replace with back-up")
#         elif faulty_count > 1:
#             print(f"Too many faulty items in {category}, skipping further checks")
#             break
#         else:
#             print(f"{category} : {working_count} are working")
#             continue

# category_report(inventory)

#
# employeesA = {
#     101:{"name": "Ion","role": "Programer"},
#     102:{"name":"Maria", "role":"Accountant"},
#     103:{"name":"Laur", "role":"Economist"}
# }
#
# employeesB={
#     201:{"name": "Ion","role": "Sales Manager"},
#     202:{"name":"Maria", "role":"Sales expert"},
#     203:{"name":"Laur", "role":"Cashere"}
# }
#
# count = len(employeesA)
# print(f"There are {count} employees")
#
# employeesA[102]["role"] = "Senior Analyst"
# employeesA[104]={"name":"Liviu","role":"Technician"}
# print(employeesA)
#
# for emp_id, info in employeesA.items():
#     print(f"ID: {emp_id}, Name: {info['name']}, Role: {info['role']}")
#
# def get_role(emp_id, data):
#     if emp_id in data:
#         return data[emp_id]["role"]
#     else:
#         return "Not found!"
#
#
# merged = {**employeesA, ** employeesB}
# print("Merged:",merged)
#
# target_id = 201
# if target_id in merged:
#     print("Employee Ready!")
# else:
#     print("Not found!")

#
# seats= array.array('i',[101,102,103,104,105,106,107,108])
# print(f"Total seats :" , len(seats))
# seats[3]=110
# print("After move ", seats)
# print("First 4 seats are: " , seats[0:4])
# print("Last 3 seats are : ", seats[-3:])
#
# for seat in seats:
#     if seat in (102,106):
#         print(f" Seat {seat} - Reserved")
#     else:
#         print(f" Seat {seat}- Free")
# 
#
# reserved = ('i', [102,106,108])
# def next_available(start_seat, seats, reserved):
#     for seat in seats:
#         if seat>=start_seat and seat  not in reserved:
#             return seat
#     return None
#
#
# result = next_available(105,seats,reserved)
# print(result)