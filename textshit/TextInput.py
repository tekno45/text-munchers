
# Take in text and award points. All point awards coming from text will be in this file

def points4words (text, bonus_list, multiplier=1):
    bonus_points = 0
    length = len(text)
    points = length

    # Aaron hall, fastest way to find a string inside a string
    for word in bonus_list:
        if word in bonus_list:
            bonus_points+=1
            

    # award bonus points for each bonus word that appears. One bonus per bonus word

    exp= (points+ bonus_points * multiplier)

    # return a tuple of points and bonus points, this bubble of points will be used on all point receivers
    return exp



# os.chdir("d:/and")
# x = open("data.csv")
if __name__ == "__main__":

    bonuslist = ["roar", "dumb", "eat"]

# for row in csv.reader(x):
# bonuslist.append(row[0])
# bonusset = set(bonuslist)
# bonusset = list(bonusset)
    text = "nsdjksdfpfnklssdfha;'sldkasdinoredroadnklfssnfnaklsnikldumbmlasdaasbmkeeareat"
    result = points4words(text, bonuslist)
    print(result)

# print (bonusinstuff)
# print(bonuspoints)
# stuff = input("Enter words: ")
# bonuswords = ["butts", "stuff"]
# bonuspoints = 0
