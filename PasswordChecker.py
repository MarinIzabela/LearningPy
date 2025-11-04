# Input Password from user
password = input("Insert your password to check its strenght: ")
strenght = 0
if len(password) >= 8:
    strenght += 1
else:
    strenght += 0

if "!" in password:
    strenght += 1
else:
    strenght += 0
if "@" in password:
    strenght += 1
else:
    strenght += 0
if "#" in password:
    strenght += 1
else:
    strenght += 0

if strenght >= 2:
    print("The password is strong!")
else:
    print("The password is week !")
