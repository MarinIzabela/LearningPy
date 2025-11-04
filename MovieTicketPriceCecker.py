
base_price = 500

age = int(input("Enter your age : "))
loyalty_card = input("Do you have a loyalty card? (yes/no) : ").lower()

if loyalty_card not in ["yes", "no"]:
    print("Invalid input for loyalty card . Please enter 'yes' or' no'!")
else:
    if age < 18:
        discount = 0.50
    elif 18 <= age <= 60:
        discount = 0.20
    elif age > 60:
        discount = 0.30
    else:
        discount = 0

if loyalty_card == "yes":
    discount += 0.05

final_price = base_price * (1 - discount )
print("\n.........Ticket Details.............")
print(f"Base Ticket Price:{base_price} $")
print(f"Discount applied : {discount*100:.0f}%")
print(f"Final Price {final_price:.2f}$.")