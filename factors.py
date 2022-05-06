#file that contains the class object for NPC's and adversities

import attributes as att

participants = {
    "character": [],
    "enemy": []
}


class Sheet():
    def __init__(self):
        self.abilities = []
        self.name = []
        self.hp = ''
        self.armor = att.armor()
        pass

def getInfo(file):
    while True:
        line = file.readline()
        if not line:
            break
        else:
            key = line.split(':')[0]
            participants[key].append(fillSheet(file))
            
    return participants

def fillSheet(file):
    sheet = Sheet()
    while True:
        line = file.readline()
        if not line or '=' in line:
            break
        else:
            try:
                key = line.split(':')[0]
                val = line.strip()
                setattr(sheet, key, val.split()[1:])
            except Exception as e:
                print(e)

    return sheet

def getStats(file):

    pass
def getInv():
    pass

def getStats():
    pass
