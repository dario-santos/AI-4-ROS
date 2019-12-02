
class Object:

    def __init__(self, name, category):
        self.name = name
        self.category = category

        def setName(self, name):
            self.name = name

        def setCategory(self, category:Category):
            self.category = category

        def getName(self):
            return self.name

        def getCategory(self):
            return self.category

class Category(Enum):
    door     = 0
    bed      = 1
    book     = 2
    chair    = 3
    computer = 4
    person   = 5
    table    = 6
    mistery  = 7
