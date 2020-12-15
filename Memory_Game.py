import random
import time
import os

def generate_sequence(diff):
    secret_list = random.sample(range(1, 101), diff)
    time.sleep(0.7)
    os.system("cls")
    return secret_list


def get_list_from_user(diff):
    user_list=[]
    for i in range (1, diff+1):
        user_list.append(i)
    print(" Enter", diff, "numbers between 1 to 101:")
    for i in range (1, diff+1):
        print("enter number", i, end='')
        user_list[i-1] = int(input(" here: "))
    return(user_list)


def is_list_equal(diff):
     return (generate_sequence(diff)) == (get_list_from_user(diff))


def play(diff):
   print("\nWelcome to the memory game! \n")
   print(is_list_equal(diff))

