
class Muncher:
    def __init__(self):
        self.exp = 0
        self.level = 0
        self.name = ""

    # add contents of tuple to exp, will return true for now, will add error handling later
    def feed(self, points):
        self.exp = points[0] + points[1]
        return True

    # returns attributes needed to save monster. List is returned and will be run through a csv writer
    def muncher_save(self):
        export = [self.name, self.exp, self.level]
        return export
# x = Muncher()
    # os.chdir("d:/and")
    # y = open("data.csv")
    # words = []
    # for row in csv.reader(y):
    # words.append(row[0])

    # x.Feed(points4words(input(), set(words)))
