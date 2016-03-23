
#Aaron hall, fastest way to find a string inside a string
def checkwrds(wrds,stuffs):
    return set(wrds).intersection(stuffs.split())

#Take in text and award points
def points4words ():

stuff = input("Enter words: ")
bonuswords = ["butts", "stuff"]
bonuspoints = 0

#for word in checkwrds(bonuswords,stuff):
 #   bonuspoints = bonuspoints +1

bonusinstuff  = [stuff.count(word) for word in bonuswords]

for x in bonusinstuff:
    if x >= 1:
        bonuspoints = bonuspoints +1
points = len(stuff)
message = "Your text is worth {} points!"
print(message.format(int(points)))

if bonuspoints > 0:
    bonusmessage  = "WOAH you earned {} bonus points!"
    print(bonusmessage.format(bonuspoints))

print (bonusinstuff)
print(bonuspoints)





