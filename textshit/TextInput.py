
# Take in text and award points. All point awards coming from text will be in this file

def points4words (text, bonus):
    bonuspoints = 0
    length = len(text)
    points = length

    # Aaron hall, fastest way to find a string inside a string
    bonusinstuff = [text.count(word) for word in bonus]

    # award bonus points for each bonus word that appears. One bonus per bonus word
    for x in bonusinstuff:
        if x >= 1:
            bonuspoints += 1

    bubble = points, bonuspoints

    # return a tuple of points and bonus points, this bubble of points will be used on all point receivers
    return bubble

# os.chdir("d:/and")
# x = open("data.csv")
# bonuslist = ["roar", "dumb", "eat"]
# for row in csv.reader(x):
# bonuslist.append(row[0])
# bonusset = set(bonuslist)
# bonusset = list(bonusset)
# points4words(input("Enter words: "), bonusset)


# print (bonusinstuff)
# print(bonuspoints)
# stuff = input("Enter words: ")
# bonuswords = ["butts", "stuff"]
# bonuspoints = 0
