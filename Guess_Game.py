import random

def generate_number(diff):
    secret_number = random.randint(1, diff)
    return secret_number

def get_guess_from_user(diff):
    # you can put the print message into the input
    print("Please guess a number between 1 to", diff, end = '')
    user_guess = input(": ")
    if not user_guess.isdigit():
        print("your guess must be a digit")
        get_guess_from_user(diff)
        exit()
    int_user_guess = int(user_guess)
    if not int_user_guess in range(1, 11):
        print("Your choice is invalid. Your guess must be between 1 to 10")
        get_guess_from_user(diff)
        exit()
    return (int_user_guess)

def compare_results(diff):
    return get_guess_from_user(diff) == generate_number(diff)

def play(diff):
    print("\nWelcome to the Guess Game! \n")
    print(compare_results(diff))

