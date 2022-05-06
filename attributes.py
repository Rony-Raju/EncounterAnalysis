#file that contains the class object for PC's and assets

#array with name, dice, finesse, damage type, and range
class weapon:
    def __init__(self, traits):
        self.name = traits[0]
        self.damage = traits[1]
        self.finesse = traits[2]
        self.attributes = traits[3]
        self.range = traits[4]

#array with spells, weapon stats, summons, and charges
class magicItems():
    def __init__(self, traits):
        self.spells = traits[0]
        if traits[1]:
            self.weapon = weapon(traits[1])
        self.summons = traits[2]
        self.charges = traits[3]

#array with type, AC, maximum dex mod, stealth mod, and type resistance
class armor():
    def __init__(self, traits):
        self.type = traits[0]
        self.baseAC = traits[1]
        self.maxDex = traits[2]
        self.stealth = traits[3]
        self.resistances = traits[4]

#speed, carry weight, and travel speed
class vehicle():
    def __init__(self, traits):
        self.speed = traits[0]
        self.carryWeight = traits[1]
        self.speed = traits[2]



#weapons, magic items, armor, vehicles, and wealth
class inventory():
    def __init__(self, items):
        self.weapons = [weapon(i) for i in items[0] ]
        self.magicItems = [magicItems(i) for i in items[1] ]
        self.armor = armor(items[2])
        self.vehicles = [vehicle(i) for i in items[3] ]
        self.wealth = items[4]
