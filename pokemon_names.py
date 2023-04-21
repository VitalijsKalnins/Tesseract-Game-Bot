## Imports
import difflib

## Pokemon Names List
poke_names = []

with open("data/pokemon_names.txt", "r") as file:
    for line in file:
        poke_names = line.split(", ")

## Pokemon with the Name Closest to Specified String
def closest_name(name):
    return difflib.get_close_matches(name, poke_names, n=1)[0]