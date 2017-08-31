import os; import csv;
from Munchers import Muncher; from TextInput import points4words

# monsters will be loaded into the pen, passed bubbles of points. Interactions will be done here
monName = input("Name your monster: ")

Mon1 = Muncher()
Mon1.name = monName

os.chdir("d:/and")
txt = open("data.csv")

bonuswords = []

for row in txt:
    bonuswords.append(row[0])

bonuswords =  set(bonuswords)

choice = True

while choice == True:
    if input("Feed him? Y/N").lower() == "y":
        Mon1.Feed(points4words(input("Enter your words: "),bonuswords))
    else:
        choice = False
        message = "{} gained {} exp"
        print(message.format(Mon1.name,Mon1.exp))

