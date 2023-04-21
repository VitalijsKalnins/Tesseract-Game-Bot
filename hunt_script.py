## Imports
import keyboard
from player import player
from pokemon import pokemon


## Tracking Move PP
pp0 = 40
pp1 = 15

## Control Variables
hunting = False
encountering = False
switched = False
stopped = False
checked = True

## Desired Pokemon to Hunt
desired = pokemon("Magikarp", "ANY", "Jolly", [31, 20, 31, "ANY", 20, 20], "ANY", "ANY")
desired2 = pokemon("Gyarados", "ANY", "Jolly", [31, 20, 31, "ANY", 20, 20], "ANY", "ANY")

## Configuration -> Repel Tricking
repelling = False

## Count Variables
desired_count = 0
total_count = 0


## Callback to Enable / Disable Script
def switch_mode():
    ## Switch 'hunting'
    global hunting
    hunting = not hunting

    if not hunting:
        print(f"TOTAL CAUGHT: {total_count}")
        print(f"DESIRED CAUGHT: {desired_count}")
keyboard.add_hotkey("x", switch_mode)


while True:
    while hunting:
        if player.is_battling():
            ## Stop Moving Once in Encounter
            if not stopped:
                player.stop_move()
                stopped = True

            if player.allowed_move():
                if not encountering:
                    ## Get Name of Pokemon in Current Encounter
                    encountering = player.get_battling()

                    if encountering != desired.name and encountering != desired2.name:
                        player.run()
                    else:
                        checked = False
                else:
                    if not switched:
                        player.switch_member()
                        switched = True

                    elif not player.health_battling_low():
                        if player.is_battling():
                            player.use_move(0)
                            pp0 -= 1

                    elif not player.sleeping_battling():
                        if player.is_battling():
                            player.use_move(1)
                            pp1 -= 1

                    else:
                        player.has_item("pokeball", False)
                        player.use_ball()     

        else:
            ## Reset Control Variables
            encountering = False
            switched = False
            stopped = False

            ## Check Caught Preview
            while not checked:
                ## Check if Preview is Open First!
                if player.is_preview_open():
                    ## Reset Caught Check Control Variable
                    checked = True

                    caught_desired = player.check_caught(desired)

                    ## Increment Count Variables
                    if caught_desired:
                        desired_count += 1
                    total_count += 1

            ## Repel Logic
            if repelling:
                if not player.check_repel():
                    player.use_repel()

            ## Move PP Logic
            if pp0 <= 30:
                if player.has_item("ether", False):
                    player.use_pp_item(5, 0)
                    pp0 += 10
            if pp1 <= 5:
                if player.has_item("ether", False):
                    player.use_pp_item(5, 1)
                    pp1 += 10

            ## Move 
            player.hold_key("w", 0.1725)
            player.hold_key("s", 0.1725)
