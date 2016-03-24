from TextInput import points4words
import os
import csv
class Muncher:
    def __init__(self):
        self.exp = 0
        self.level = 0

    def Feed(self, bubble):
        for x in bubble:
            self.exp = self.exp + x
        return True

x = Muncher()
os.chdir("d:/and")
y = open("data.csv")
words = []
for row in csv.reader(y):
    words.append(row[0])

x.Feed(points4words(input(), set(words)))


