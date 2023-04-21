import pydirectinput
import keyboard

from player import player
from reader import reader
from pokemon import pokemon

desired = pokemon("Rattata", "Run Away", "Adamant", [31, 24, 31, "ANY", 24, 24], "ANY", "Fire")

def test():
    print(reader.read_pixel(1544, 558))
keyboard.add_hotkey("x", test)


k=input("press close to exit\n")    