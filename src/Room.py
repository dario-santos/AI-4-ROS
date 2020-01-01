import RoomObject

class Room:
    
    def __init__(self, objects):
        self.connectedTo = ""
        self.objects = objects

    def SetConnectedTo(self, value):
        self.connectedTo = value
    
    def GetConnectedTo(self):
        return self.connectedTo
    
    def AddObject(self, name):
        info = name.split("_", 1)
        if len(info) != 2: 
            return

        for _, o in enumerate(self.objects):
            if o.GetName() == info[1]:
                return
            
        # Categoria, Nome
        obj = RoomObject.RoomObject(RoomObject.Category.GetCategory(info[0]), info[1])
        self.objects.append(obj)

    def RemoveObject(self, name):
        info = name.split("_", 1)
        obj = RoomObject.RoomObject(info[0], info[1])

        self.objects.remove(obj)

    def GetObjectByName(self, name):
        for _, o in enumerate(self.objects):
            if o.GetName() is name:
                return o
        return None
        
    def GetObjectsByCategory(self, category):
        objects = []
        for _, o in enumerate(self.objects):
            if o.GetCategory() is category:
                objects.append(o)
        return objects

    def IsOccupied(self):
        for _, o in enumerate(self.objects): 
            if o.GetCategory() == RoomObject.Category.person:
                return True
        return False

    def GetRoomType(self):
        nOfBeds = len(self.GetObjectsByCategory(RoomObject.Category.bed))
        nOfTables = len(self.GetObjectsByCategory(RoomObject.Category.table))
        nOfChairs = len(self.GetObjectsByCategory(RoomObject.Category.chair))



        if nOfBeds == 1 and self.connectedTo == "":
            return RoomType.single
        elif nOfBeds > 0 and self.connectedTo != "":
            return RoomType.suite
        elif nOfBeds == 2:
            return RoomType.double
        elif nOfTables == 1 and nOfChairs > 2:
            return RoomType.meeting
        return RoomType.generic

class RoomType:
    size = 5
    none   = 0
    single   = 1
    double   = 2
    suite    = 3
    meeting  = 4
    generic  = 5

    @staticmethod
    def GetType(type_name):
        if type_name == 'single':
            return Room.single
        elif type_name == 'double':
            return RoomType.double
        elif type_name == 'suite':
            return RoomType.suite
        elif type_name == 'meeting':
            return RoomType.meeting
        elif type_name == 'generic':
            return RoomType.generic
        return 0

    @staticmethod
    def GetName(type_index):
        if type_index is RoomType.single:
            return "single"
        elif type_index is RoomType.double:
            return "double"
        elif type_index is RoomType.suite:
            return "suite"
        elif type_index is RoomType.meeting:
            return "meeting"
        elif type_index is RoomType.generic:
            return "generic"
        return "None"
