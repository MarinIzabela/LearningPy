original_price = float(input("Enter the original price in dollars: $"))
apply_discount = lambda price: price * 0.90 if price > 100 else price*0.95

def calculate_tax(price):
    tax_rate = price * 0.07 if price > 100 else 0.05
    tax_amount = tax_rate * price
    final_price = price + tax_amount
    return final_price, tax_amount


def final_price(price):
    discounted_price = apply_discount(price)
    adjusted_price, tax_amount = calculate_tax(discounted_price)
    return discounted_price, adjusted_price, tax_amount

discounted, final_adjusted, tax_deducted = final_price(original_price)

discount_applied = "10%" if original_price>100 else "5%"

print(f"Original price : {original_price:.2f}")
print(f"Discount applied : {discount_applied}")
print(f"Price after discount : {discounted:.2f}")
print(f"Tax deducted : {tax_deducted:.2f}")
print(f"Final adjusted price : {final_adjusted:.2f}")