## Imports
import pydirectinput
import time

from reader import reader
from pokemon_names import closest_name
from abilities import closest_ability
from natures import closest_nature


## Click Macro Function
def click_at(XOrig, YOrig):
    pydirectinput.moveTo(XOrig, YOrig)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()


## Player Class
class player:
    ## Fetch Player's Money
    def get_money():
        ## Read Player Money -> Return Digits of Money as Integer
        read_data = reader.read_string(37, 1056, 92, 18)
        return int(''.join(filter(str.isdigit, read_data)))


    ## Check if Player is Battling
    def is_battling():
        ## Read Pixel of Battle Indicator
        col = reader.read_pixel(658, 326)

        if ((col[0] == 194) and (col[1] == 26) and (col[2] == 26)):
            return True
        else:
            return False


    ## Fetch Name of Pokemon in Encounter
    def get_battling():
        ## Read Name of Pokemon in Encounter
        read_data = reader.read_string(888, 328, 200, 24)
        return closest_name(read_data[5:])


    ## Check if Player is Allowed to Move
    def allowed_move():
        ## Read Pixel of Battle Indicator
        col = reader.read_pixel(1230, 656)

        if ((col[0] == 193) and (col[1] == 193) and (col[2] == 193)):
            return True
        else:
            return False  


    ## Use Move in Battle given Index
    def use_move(index):
        ## Click Fight
        click_at(1230, 656)

        ## Click Move
        click_at(1273, (384 + (54 * index)))


    ## Run from Encounter
    def run():
        ## Click Run Button
        click_at(1334, 738)

    
    ## Check if Player has Item
    def has_item(item_name, close):
        ## Open Inventory
        click_at(22, 867)

        ## Click Reset Search
        click_at(1081, 393)

        ## Click Search
        click_at(1003, 393)
        
        ## Search for Item
        pydirectinput.write(item_name)

        ## Read Colour of Item Edge
        px_col = reader.read_pixel(894, 420)

        ## Close Inventory Check
        if close:
            ## Close Inventory
            click_at(1111, 393)

        ## Check Item Edge Colour
        if (px_col[0] == 87 and px_col[1] == 86 and px_col[2] == 90):
            return True
        else:
            return False


    ## Use PP Item
    def use_pp_item(party_num, move_num):
        ## Click Use Item
        click_at(741, 437)

        ## Click Party Member 
        click_at((800 + (party_num * 64)), 552)

        ## Click Move
        click_at(952, (492 + (move_num * 40)))

        ## Close Party Member Select
        click_at(1167, 492)

        ## Close Inventory
        click_at(1111, 393)


    ## Use Health Item
    def use_health_item(party_num):
        ## Click Use Item
        click_at(741, 437)

        ## Click Party Member
        click_at((800 + (party_num * 64)), 552)

        ## Close Inventory
        click_at(1111, 393)


    ## Use Ball
    def use_ball():
        ##Click Use Item
        click_at(741, 437)

        ## Close Inventory
        click_at(1111, 393)


    ## Switch Pokemon During Battle;  TO-DO: Change this to support any party member (not just last)
    def switch_member():
        ## Click Switch Pokemon
        click_at(1316, 656)

        ## Click Pokemon
        click_at(1316, 544)


    ## Check if Pokemon in Encounter has Low Health
    def health_battling_low():
        ## Read Colour
        col = reader.read_pixel(622, 398)

        ## Check if Red Colour
        if ((col[0] >= 129)  and (col[1] <= 35) and (col[2] <= 15)):
            return True
        else:
            return False


    ## Check if Pokemon in Encounter is Sleeping
    def sleeping_battling():
        ## Read Colour
        col = reader.read_pixel(762, 368)

        ## Check if Colour Matches Sleep Label
        if ((col[0] == 173) and (col[1] == 173) and (col[2] == 198)):
            return True
        else:
            return False


    ## Check for Active Repel
    def check_repel():
        ## Read Colours
        col0 = reader.read_pixel(192, 15)
        col1 = reader.read_pixel(225, 15)
        col2 = reader.read_pixel(260, 15)

        ## Check All Colours
        if ((col0[0] == 255) and (col0[1] == 255) and (col0[2] == 255)):
            return True
        elif ((col1[0] == 255) and (col1[1] == 255) and (col1[2] == 255)):
            return True
        elif ((col2[0] == 255) and (col2[1] == 255) and (col2[2] == 255)):
            return True
        return False


    ## Use Repel
    def use_repel():
        ## Activate Repel
        player.hold_key("1", 0.03)


    ## Check if Preview Is Open
    def is_preview_open():
        col = reader.read_pixel(1544, 558)

        ## Check if Colour Matches Preview Frame
        if ((col[0] == 43) and (col[1] == 47) and (col[2] == 57)):
            return True
        else:
            return False


    ## Check Caught Preview
    def check_caught(desired):
        ## Scan Ability Name
        ability = closest_ability(reader.read_string(1542, 665, 144, 18).rstrip())

        ## Scan Nature Name
        nature = closest_nature(reader.read_string(1542, 706, 144, 18).rstrip())

        ## Scan Hidden Power
        hidden_power = (reader.read_string(1542, 791, 144, 18).rstrip())

        ## Scan IVs
        ivs = []
        for i in range(0, 6):
            iv = reader.read_num(1763, (718 + (i * 16)), 15, 15)
            ivs.append(iv)

        ## Check Against Desired
        if not (desired.ability == ability or desired.ability == "ANY"):
            return False
        elif not (desired.nature == nature or desired.nature == "ANY"):
            return False
        elif not (desired.hidden_power == hidden_power or desired.hidden_power == "ANY"):
            return False

        ## Check IVs against Desired
        for i in range (0, 6):
            if not (desired.ivs[i] <= ivs[i] or desired.ivs[i] == "ANY"):
                return False

        return True


    ## Hold Key For
    def hold_key(key, duration):
        pydirectinput.keyDown(key)
        time.sleep(duration)
        pydirectinput.keyUp(key)


    ## Release All Movement Keys
    def stop_move():
        pydirectinput.keyUp("w")
        pydirectinput.keyUp("a")
        pydirectinput.keyUp("s")
        pydirectinput.keyUp("d")