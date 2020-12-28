import random
import time
import os
from myAbstract import MyAbstract

class Memory_Game(MyAbstract):

    def __init__(self, diff):
        self.diff = diff

    def welcome(self):
        print("\n Welcome to the memory game! \n")

    def get_input_from_pc(self):
        secret_list = random.sample(range(1, 101), self.diff)
        time.sleep(0.7)
        os.system("cls")
        return secret_list

    def get_input_from_user(self):
        user_list=[]
        for i in range (1, self.diff+1):
            user_list.append(i)
        print(" Enter", self.diff, "numbers between 1 to 101:")
        for i in range (1, self.diff+1):
            print("enter number", i, end='')
            user_list[i-1] = int(input(" here: "))
        return(user_list)


    def compare(self):
         return (self.get_input_from_pc()) == (self.get_input_from_user())


    def play(self):
        self.welcome()
        return(self.compare())


