## Imports
import difflib

## Abilities List
moves = []

with open("data/moves.txt", "r") as file:
    for line in file:
        moves = line.split(",")


## Move Closest to Specified String
def closest_move(name):
    return difflib.get_close_matches(name, moves, n=1)[0]