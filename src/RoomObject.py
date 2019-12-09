
class RoomObject:

    def __init__(self, category, name):
        self.name = name
        if category == 'person':
            self.category = Category.person
        elif category == 'door':
            self.category = Category.door
        elif category == 'bed':
            self.category = Category.bed
        elif category == 'book':
            self.category = Category.book
        elif category == 'chair':
            self.category = Category.chair
        elif category == 'computer':
            self.category = Category.computer
        elif category == 'table':
            self.category = Category.table
        else:
            self.category = Category.mistery

    def SetName(self, name):
        self.name = name

    def SetCategory(self, category):
        self.category = category

    def GetName(self):
        return self.name

    def GetCategory(self):
        return self.category

class Category:
    door     = 0
    bed      = 1
    book     = 2
    chair    = 3
    computer = 4
    person   = 5
    table    = 6
    mistery  = 7
