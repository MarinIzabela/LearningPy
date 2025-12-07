class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    # dunder method
    def __str__(self):
        return f"{self.name} - {self.price:.2f}"



class BestBuyCart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        self.items.append((product, quantity))

    def total_price(self):
        total = 0
        for item,quantity in self.items:
            total += item.price * quantity
        return total

    def __str__(self):
        cart_summary = "\n Best Buy Shopping Cart\n"
        for item, quantity in self.items:
            cart_summary += f"{quantity} * {item}\n"
        cart_summary += f"\n Total Price: $ {self.total_price():.2f} USD"
        return cart_summary

class BestBuyDiscountCart(BestBuyCart):
    def add(self, product, quantity=1 , discount = 0):
        discounted_price = product.price -( product.price * discount/100)
        discounted_product = Product(product.name, discounted_price)
        super().add( discounted_product, quantity)

laptop = Product("Laptop", 500)
mouse = Product("Mouse", 500)
tv = Product("TV", 500)

best_buy_cart = BestBuyDiscountCart()
best_buy_cart.add(laptop, quantity=1, discount=15)
best_buy_cart.add(mouse, quantity=1, discount=10)
best_buy_cart.add(mouse, quantity=2)
best_buy_cart.add(tv, quantity=3)

print(best_buy_cart)
print("\n Thank you for shopping with Best Buy Shopping Cart.")