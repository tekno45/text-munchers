

def checkwrds(wrds,stuffs):
    return set(wrds).intersection(stuffs.split())

#Take in text and award points

stuff = input("Enter words: ")
bonuswords = ["butts", "stuff"]
bonuspoints = 0
for word in checkwrds(bonuswords,stuff):
    bonuspoints = bonuspoints +1
points = len(stuff) + bonuspoints

message = "Your text is worth {} points!"

print(message.format(int(points)))


