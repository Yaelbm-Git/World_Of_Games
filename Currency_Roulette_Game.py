import os
os.getcwd()
from exchangeratesapi import Api

api = Api()


def get_money_interval(diff):
    api.get_rates()
    t = api.get_rate('USD', target='ILS')
    range1 = (t-(5-diff))
    range2 = (t+(5-diff))
    return (range1, range2)

def get_guess_from_user(diff):
    user_guess = input("Guess what the ILS rate is for 1 Dollar:")
    return float(user_guess)

def play(diff):
    print(" \n Welcome to Currency Roulette Game! \n")
    myrange = get_money_interval(diff)
    low_lim = myrange[0]
    high_lim = myrange[1]
    if low_lim <= get_guess_from_user(diff) <= high_lim:
        print("True")
    else:
        print("False")



