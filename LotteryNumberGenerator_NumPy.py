import numpy as np

class LotteryGame:
    def __init__(self):
        self.winning_number=None

    def generate_lottery_number(self):
        number=np.random.uniform(1,49)
        self.winning_number=round(number)

    def get_user_guess(self):
        while True:
            try:
                guess= int(input("Enter your  Lottery number: "))
                if 1<=guess<=49:
                    return guess
                else:
                    print("Please enter your Lottery number:")
            except ValueError:
                print(" Invalid input.Please enter your Lottery number:")

    def check_result(self,user_number):
        print("The Lottery number is ",self.winning_number)
        if user_number==self.winning_number:
            print("You win!")
        else:
            print("You lose!")



game = LotteryGame()
game.generate_lottery_number()
user_guess=game.get_user_guess()
game.check_result(user_guess)