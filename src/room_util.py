import RoomObject
import Room

room_nomenclature_prefix = 'Room '

def getNumber(x, y):
    if x >= -0.7 and x <= 18.7 and y <= 0.2 and y >= -1.7:
        return 1
    elif x >= 3.1 and x <= 5.5 and y <= 6.5 and y >= 0.5:
        return 2
    elif x >= 3.2 and x <= 18.7 and y <= 8.9 and y >= 6.8:
        return 3
    elif x >= 10.9 and x <= 13.7 and y <= 6.5 and y >= 0.6:
        return 4
    elif x >= -0.7 and x <= 2.7 and y <= 3.9 and y >= 0.5:
        return 5
    elif x >= -0.7 and x <= 2.7 and y <= 8.9 and y >= 4.3:
        return 6
    elif x >= -0.7 and x <= 4.0 and y <= 12.6 and y >= 9.3:
        return 7
    elif x >= 4.3 and x <= 8.9 and y <= 12.6 and y >= 9.3:
        return 8
    elif x >= 9.3 and x <= 14.0 and y <= 12.6 and y >= 9.3:
        return 9
    elif x >= 14.3 and x <= 18.7 and y <= 12.6 and y >= 9.3:
        return 10
    elif x >= 14.1 and x <= 18.7 and y <= 6.4 and y >= 3.7:
        return 11
    elif x >= 14.1 and x <= 18.7 and y <= 3.3 and y >= 0.5:
        return 12
    elif x >= 6.0 and x <= 8.0 and y <= 6.4 and y >= 0.6:
        return 13
    elif x >= 8.4 and x <= 10.5 and y <= 6.4 and y >= 0.6:
        return 14
    return -1

def getNomenclature(x, y):
    return room_nomenclature_prefix + str(getNumber(x, y))

def isHall(roomNumber=-1, roomName=''):
    if roomName != '':
        return roomName == 'Room 1' or roomName == 'Room 2' or roomName == 'Room 3' or roomName == 'Room 4' 
    if roomNumber != -1:
        return roomNumber <= 4 and roomNumber >= 1

    raise Exception("Invalid params")

def getProbabilityOfFindingPerson(G, rooms):
    numberOfPeople = 0
    numberOfPeopleInRoom = 0.0
    prob = 0
    
    for i in G:
        numberOfPeople += len(rooms[i].GetObjectsByCategory(RoomObject.Category.person))
        if not isHall(i):
            numberOfPeopleInRoom += len(rooms[i].GetObjectsByCategory(RoomObject.Category.person))

    if numberOfPeople == 0:
        return "There\'s no known people."

    prob = (numberOfPeopleInRoom * 100)/numberOfPeople

    if prob > (1 - prob):
        return "There\'s a bigger probability of finding a person in a room."
    
    return "There\'s a bigger probability of finding a person in a hall."

def getProbabilityOfBeingOccupied(G,rooms):
    personsOnHalls = 0
    personsOnRooms = 0
    nOfHalls = 0.0
    nOfRooms = 0.0
    probOfHalls = 0.0
    probOfRooms = 0.0
    for i in G:
        if rooms[i].GetObjectsByCategory(RoomObject.Category.person):
            if isHall(roomName=i):
                personsOnHalls+=1
                nOfHalls+=1
            else:
                personsOnRooms+=1
                nOfRooms+=1
        else:
            if isHall(roomName=i):
                nOfHalls+=1
            else:
                nOfRooms+=1

    if nOfHalls != 0:
	    probOfHalls = (personsOnHalls / nOfHalls) * 100
    if nOfRooms != 0:
	    probOfRooms = (personsOnRooms / nOfRooms) * 100

    if probOfHalls == probOfRooms:
	    return "The probability of being occuped is the same (%.0f%%)" % probOfHalls
    elif probOfHalls > probOfRooms:
	    return "There\'s a bigger probability a hall be occupied (%.0f%%)" % probOfHalls
    return "There\'s a bigger probability a room be occupied (%.0f%%)" % probOfRooms

def getProbabilityComputer(G, rooms):
    count_rooms = [0] * Room.RoomType.size
    count_pc_rooms = [0.0] * Room.RoomType.size
    prob_rooms = [0.0] * Room.RoomType.size

    for i in G:
        room = rooms[i]

        t = room.GetRoomType()
        if t is not Room.RoomType.none:
            count_rooms[t - 1] += 1
            if room.GetObjectsByCategory(RoomObject.Category.computer):
                count_pc_rooms[t - 1] += 1
        
    for i,o in enumerate(count_rooms):
        if o != 0:
            prob_rooms[i] = count_pc_rooms[i] / o

    p = max(prob_rooms)
    if p == 0.0:
        return "There are no known computers"

    index = prob_rooms.index(p) + 1

    return "You go to the room type %s" % Room.RoomType.GetName(index)
    
def getNumberOfBooks(rooms):
    cnt = 0
    for _, room in enumerate(rooms.values()):
        cnt += len(room.GetObjectsByCategory(RoomObject.Category.book))
    return cnt
