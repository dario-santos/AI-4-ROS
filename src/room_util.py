def GetNumber(x, y):
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
    else:
        return -1

def IsHall(roomNumber):
    return roomNumber <= 4 and roomNumber >= 1

