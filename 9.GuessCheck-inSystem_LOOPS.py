#Guest check-in Program
print("Welcome to the Guest check-in System !\n")
max_guest = input("Enter the maxim guest allowed : ")

#   validate the input for maxim guest
if max_guest.isdigit():
    max_guest = int(max_guest)
else:
    print("Invalid number!Please input a valid number!!")
    exit()

guest_count = 0
while guest_count < max_guest:
    print(f"Guest  : {guest_count + 1}")
    guest_name = input("Please insert the name of the guest!")
    age = input("Please enter the guest age!")
    if age.isdigit():
        guest_age = int(age)
    else:
        print("Invalid age! Try again!")
        continue

    print("Does the guest have an reservation yes/no? ")
    reservation = input().strip().lower()
    if reservation == "yes":
        print(f"Guest {guest_name} is succesfully checked!")
        guest_count += 1
    elif reservation == "no":
        if guest_age >= 18:
            print(f" Guest {guest_name} is allowed to check-in without a reservation!")
            guest_count += 1
        else:
            print(f"Guest {guest_name} is under 18 and cannot be checked-in without a reservation!  ")
    else:
        print("Invalid input for the reservation! Try again!")



print("Check-in complete! Maximum guests reached")



