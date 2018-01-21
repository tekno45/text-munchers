import csv
import os
from Munch import Munchers
from textshit import TextInput



# monsters will be loaded into the pen, passed bubbles of points. Interactions will be done here
# Monsters will have labels, pen will grab proper word list file based on label


monName = input("Name your monster:")
Mon1 = Munchers.Muncher()
Mon1.name = monName

# opening file for bonuswords
os.chdir("d:/and")
txt = open("data.csv")

bonuswords = []

for row in txt:
    bonuswords.append(row[0])

bonuswords = set(bonuswords)

choice = True
reader = csv.reader("emails.csv")

while choice:
    if input("Feed him? Y/N").lower() == "y":
        x = input("Enter your words: ")
        x = x.strip()
        Mon1.feed(TextInput.points4words(x, bonuswords))
    else:
        choice = False
        message = "{} gained {} exp"
        print(message.format(Mon1.name, Mon1.exp))

