import os.path
from Utils import *


def add_score(diff):
    points_of_winning = ((int(diff) * 3) + 5)
    if os.path.exists(SCORES_FILE_NAME):
        f = open(SCORES_FILE_NAME, "r")
        current_score = f.read()
        new_score = int(current_score) + points_of_winning
        f = open(SCORES_FILE_NAME, "w+")
        f.write(str(new_score))
    else:
        f = open(SCORES_FILE_NAME, "w+")
        f.write(str(points_of_winning))