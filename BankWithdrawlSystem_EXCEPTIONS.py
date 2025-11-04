class BankOfAmerica:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <=0:
                raise ValueError('amount must be positive')
            if amount > self.balance:
                raise ValueError('Insufficient funds.')
            self.balance -= amount
            print(f" Witdrawl successful ! New ballance {self.balance:.2f}")
        except ValueError as error:
            print(error)
        except Exception:
            print("Invalid input. Please try again.")

class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def make_withdraw(self):
       amt = input(f"{self.name}Please enter amount you want to withdraw, or press 'q' to quit: ")
       if amt.lower() == 'q':
           print("Thank you for using Bank of America.")

       self.bank.withdraw(amt)

name = input("Please enter your name: ")

while True:
    try:
        initial_balance = float(input("Please enter initial balance: "))
        if initial_balance < 0:
            raise ValueError("Initial balance must be positive.")
        break

    except ValueError:
        print("Invalid input. Please try again.")



boa_account = BankOfAmerica(initial_balance)
usr = User(name, boa_account)
usr.make_withdraw()






