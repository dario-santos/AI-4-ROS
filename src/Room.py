import RoomObject

class Room:
    
    def __init__(self, objects):
        self.isSuit = False
        self.objects = objects

    def SetIsSuit(self, value):
        self.isSuit = value
    
    def GetIsSuit(self):
        return self.isSuit
    
    # Adicionar objeto
    def AddObject(self, name):
        info = name.split("_", 1)
        if len(info) != 2: 
            return

        # Verifica se o objeto ja foi adicionado
        for _, o in enumerate(self.objects):
            if o.GetName() == info[1]:
                return
            
        # Categoria, Nome
        obj = RoomObject.RoomObject(RoomObject.Category.GetCategory(info[0]), info[1])
        self.objects.append(obj)


    # Remover objeto
    def RemoveObject(self, name):
        info = name.split("_", 1)
        obj = RoomObject.RoomObject(info[0], info[1])

        self.objects.remove(obj)

    # buscar objeto pelo nome
    def GetObjectByName(self, name):
        for _, o in enumerate(self.objects):
            if o.GetName() is name:
                return o
        return None
        
    # Buscar Objetos de uma categoria
    def GetObjectsByCategory(self, category):
        objects = []
        for _, o in enumerate(self.objects):
            if o.GetCategory() is category:
                objects.append(o)
        return objects

    def IsOccupied(self):
        for _, o in enumerate(self.objects): 
            print o.GetCategory()
            if o.GetCategory() == RoomObject.Category.person:
                return True
        return False

    def GetRoomType(self):
        nOfBeds = len(self.GetObjectsByCategory(RoomObject.Category.bed))
        nOfTables = len(self.GetObjectsByCategory(RoomObject.Category.table))
        nOfChairs = len(self.GetObjectsByCategory(RoomObject.Category.chair))

        if nOfBeds == 1:
            return "single room"
        elif nOfBeds > 1 and self.isSuit:
            return "suite"
        elif nOfBeds == 2:
            return "double room"
        elif nOfTables == 1 and nOfChairs > 2:
            return "meeting room"
        else:
            return "generic room"