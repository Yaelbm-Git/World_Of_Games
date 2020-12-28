import random
from myAbstract import MyAbstract

class Guess_Game(MyAbstract):

    def __init__(self, diff):
        self.diff = diff

    def welcome(self):
        print("\nWelcome to the Guess Game! \n")

    def get_input_from_pc(self):
        secret_number = random.randint(1, self.diff)
        return secret_number

    def get_input_from_user(self):
        print("Please guess a number between 1 to", self.diff, end = '')
        user_guess = input(": ")
        if not user_guess.isdigit():
            print("your guess must be a digit")
            self.get_input_from_user()
            exit()
        int_user_guess = int(user_guess)
        if not int_user_guess in range(1, 11):
            print("Your choice is invalid. Your guess must be between 1 to 10")
            self.get_input_from_user()
            exit()
        return (int_user_guess)

    def compare(self):
        return self.get_input_from_user() == self.get_input_from_pc()

    def play(self):
        self.welcome()
        return (self.compare())

