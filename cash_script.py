import keyboard
from player import player


FARMING_CASH = False
stopped = False
encountering = False
encountered = 0
starting_cash = 0

pp = 48

def test():
    global FARMING_CASH, starting_cash

    FARMING_CASH = not FARMING_CASH
    if not FARMING_CASH:
        print(f"CASH FARMED THIS SESSION: ${player.get_money() - starting_cash}")
    else:
        starting_cash = player.get_money()
keyboard.add_hotkey("x", test)

## TO DO: ADD SHINY CLAUSE; GIVE CLOYSTER SMOKE BALL
while True:
    while FARMING_CASH:
        if player.is_battling():
            if not stopped:
                player.stop_move()
                stopped = True    

            if player.allowed_move():
                if not encountering:    
                    encountering = player.get_battling()
                    encountered += 1

                    if (encountering == "Ditto") or (encountering == "Magneton"):
                        player.run()
                else:
                    if player.is_battling():
                        player.use_move(0)
                        pp -= 1
        else:
            stopped = False
            encountering = False

            if pp == 38:
                if player.has_item("ether", False):
                    player.use_pp_item(0, 0)
                    pp += 10

            player.hold_key("w", 0.1725)
            player.hold_key("s", 0.1725)
