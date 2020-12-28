from Currency_Roulette_Game import Currency_Roulette_Game
from Guess_Game import Guess_Game
from Memory_Game import Memory_Game
from Score import add_score
from Utils import ScreenClearer


class Live():

    def welcome(self):
        username = input("Please enter your name: ")
        hello = "\nHello "
        welcome1 = " and welcome to the world of games (WOG). \nHere you can find many cool games to play. \n"
        return (hello + username + welcome1)

    def load_game(self):
        game_choice = (input("World of games menu: \n 1. Guess Game \n 2. Memory Game \n 3. Currency Roulette Game \nEnter your choice: "))
        if game_choice not in ["1", "2", "3"]:
            print("invalid choice. Please choose a number from 1 to 3. \n")
            self.load_game()
        diff = int(input("Choose a level of difficulty between 1 to 10: "))
        if game_choice == "1":
            guess_game = Guess_Game(diff)
            if guess_game.play():
                add_score(diff)
            ScreenClearer(self)
        elif game_choice == "2":
            memory_game = Memory_Game(diff)
            if memory_game.play():
                add_score(diff)
            ScreenClearer(self)
        else:
            currency_roulette_game = Currency_Roulette_Game(diff)
            if currency_roulette_game.play():
                    add_score(diff)
            ScreenClearer(self)



