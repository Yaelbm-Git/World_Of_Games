import os
os.getcwd()
from exchangeratesapi import Api
from myAbstract import MyAbstract


class Currency_Roulette_Game(MyAbstract):

    def __init__(self, diff):
        self.diff = diff

    def welcome(self):
        print(" \n Welcome to Currency Roulette Game! \n")

    def get_input_from_pc(self):
        api = Api()
        api.get_rates()
        t = api.get_rate('USD', target='ILS')
        range1 = (t-(5-self.diff))
        range2 = (t+(5-self.diff))
        return (range1, range2)

    def get_input_from_user(self):
        user_guess = input("Guess what the ILS rate is for 1 Dollar:")
        return float(user_guess)

    def compare(self):
        myrange = self.get_input_from_pc()
        low_lim = myrange[0]
        high_lim = myrange[1]
        if low_lim <= self.get_input_from_user() <= high_lim:
            return True
        else:
            return False

    def play(self):
        self.welcome()
        return(self.compare())






