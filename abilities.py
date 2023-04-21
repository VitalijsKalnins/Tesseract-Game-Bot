## Imports
import difflib

## Abilities List
abilities = []

with open("data/abilities.txt", "r") as file:
    for line in file:
        abilities.append(line.strip())


## Ability Closest to Specified String
def closest_ability(name):
    closest = difflib.get_close_matches(name, abilities, n=1)
    return closest[0]