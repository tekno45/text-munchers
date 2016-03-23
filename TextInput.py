import os
import csv
#Aaron hall, fastest way to find a string inside a string
def checkwrds(wrds,stuffs):
    return set(wrds).intersection(stuffs.split())

#Take in text and award points
def points4words (text, bonus):
    bonusinstuff = [text.count(word) for word in bonus]
    points = len(text)
    message = "Your text is worth {} points!"
    print(message.format(int(points)))
    bonuspoints = 0
    for x in bonusinstuff:
        if x >= 1:
            bonuspoints = bonuspoints +1
    if bonuspoints > 0:
        bonusmessage  = "WOAH you earned {} bonus points!"
        print(bonusmessage.format(bonuspoints))

os.chdir("d:/and")
x = open("data.csv")
bonuslist = ["roar", "dumb", "eat"]
for row in csv.reader(x):
    bonuslist.append(str(row[0].lower))

points4words(input("Enter words: "), bonuslist)


#print (bonusinstuff)
#print(bonuspoints)
#stuff = input("Enter words: ")
#bonuswords = ["butts", "stuff"]
#bonuspoints = 0












