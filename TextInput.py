import os
import csv
#Aaron hall, fastest way to find a string inside a string

#Take in text and award points
def points4words (text, bonus):
    bonuspoints = 0
    points = len(text)

    bonusinstuff = [text.count(word) for word in bonus]


    message = "Your text is worth {} points!"
    for x in bonusinstuff:
        if x >= 1:
            bonuspoints = bonuspoints +1

    bubble = points, bonuspoints
    #return a tuple of points and bonus points, this bubble of points will be used on all point recievers
    return bubble


#os.chdir("d:/and")
#x = open("data.csv")
#bonuslist = ["roar", "dumb", "eat"]
#for row in csv.reader(x):
    #bonuslist.append(row[0])
#bonusset = set(bonuslist)
#bonusset = list(bonusset)
#points4words(input("Enter words: "), bonusset)


#print (bonusinstuff)
#print(bonuspoints)
#stuff = input("Enter words: ")
#bonuswords = ["butts", "stuff"]
#bonuspoints = 0












