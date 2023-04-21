## Pokemon Class

class pokemon:
    ## Class Constructor
    def __init__(self, Name, Ability, Nature, IV_List, EV_List, Hidden_Power):
        self.name = Name
        self.ability = Ability
        self.nature = Nature
        self.ivs = IV_List
        self.evs = EV_List
        self.hidden_power = Hidden_Power