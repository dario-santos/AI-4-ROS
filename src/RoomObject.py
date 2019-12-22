class RoomObject:

    def __init__(self, category, name):
        self.name = name
        self.category = category

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
    
    @staticmethod
    def GetCategory(category_name):
        if category_name == 'person':
            return Category.person
        elif category_name == 'door':
            return Category.door
        elif category_name == 'bed':
            return Category.bed
        elif category_name == 'book':
            return Category.book
        elif category_name == 'chair':
            return Category.chair
        elif category_name == 'computer':
            return Category.computer
        elif category_name == 'table':
            return Category.table
        return Category.mistery
