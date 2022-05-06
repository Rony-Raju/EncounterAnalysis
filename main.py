import factors as fac
import attributes as att
from pprint import pprint


armor = ["light", 14, 20, "", ["cold"]]

test = att.armor(armor)

file = open('info.txt', 'r')

participants = fac.getInfo(file)

