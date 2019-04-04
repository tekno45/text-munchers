levels =[
    
    {"level":1, "exp":1000},
    {"level":2, "exp":2500}


]

class Muncher(object):
    def __init__(self, name):
        self.exp = 0
        self.level = 0
        self.name = name
        
    def feed(self, points):
        msg = []
        self.exp +=points
        msg.append("{} recieved {} exp points!".format(self.name, points))
        for level in levels:
            if self.exp >= level["exp"] and self.level != level['level']:
                self.level = level["level"]
                msg.append("{} leveled up and is now lvl {}!".format(self.name, self.level))
        print(*msg, sep="\n")
        return True

    def export(self):
        return {"name":self.name, "exp":self.exp, "level":self.level}



