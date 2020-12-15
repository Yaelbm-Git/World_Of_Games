import Currency_Roulette_Game
import Guess_Game
import Memory_Game
from Currency_Roulette_Game import play

def welcome():
    username = input("Please enter your name: ")
    hello = "\nHello "
    welcome1 = " and welcome to the world of games (WOG). \nHere you can find many cool games to play. \n"
    return (hello + username + welcome1)

def load_game():
   game_choice = int(input("World of games menu: \n 1. Guess Game \n 2. Memory Game \n 3. Currency Roulette Game \nEnter your choice: "))
   if game_choice not in range(1, 4):
       print("invalid choice. Please choose a number from 1 to 3. \n")
       load_game()
   diff = int(input("Choose a level of difficulty between 1 to 10: "))
   if game_choice == 1:
        Guess_Game.play(diff)
   elif game_choice == 2:
       Memory_Game.play(diff)
   else:
       Currency_Roulette_Game.play(diff)


