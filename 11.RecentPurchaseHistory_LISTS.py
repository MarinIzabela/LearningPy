purchase_history = [
    ["laptop", 500],
    ["mouse", 10],
    ["keyboard", 20],
    ["headphones", 20],
    ["monitor", 50],
    ["phone",300],
    ["UDB Drive", 15]

]

def show_recent_purchase(history , n=5):
    recent_purchase = history[-n:]
    print("\n Recent Purchases: ")
    for purchase in recent_purchase:
        item = purchase[0]
        price = purchase[1]
        print(f" {item}: ${price}")


def add_purchase(history , item, price):
    history.append([item,price])
    print(f"\nAdded : {item} - ${price}")


is_expensive = lambda price: "Expensive" if price>500 else "Affordable"

def total_spent(history):
    return sum(purchase[1] for purchase in history)

show_recent_purchase(purchase_history)

while True:
    item_name = input("\n Enter item name or exit to stop : ").strip()
    if item_name.lower()=="exit":
        break
    item_price = float(input("Enter item price: "))
    add_purchase(purchase_history, item_name,item_price)
    print(f"Last purchase{item_name} is {is_expensive(item_price)}.")


show_recent_purchase(purchase_history)
print(f"\n Total amount spent : {total_spent(purchase_history)}. ")