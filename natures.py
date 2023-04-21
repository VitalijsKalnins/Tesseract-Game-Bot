## Imports
import difflib

## Natures List
natures = []

with open("data/natures.txt", "r") as file:
    for line in file:
        natures.append(line.strip())

## Nature Closest to Specified String
def closest_nature(name):
    return difflib.get_close_matches(name, natures, n=1)[0]