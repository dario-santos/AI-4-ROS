import pytest
import dependencies
import sys 
sys.path.insert(0, dependencies.program_path)

from src import graph_util as g
from src import room_util as ru
from src import Room as r

def test_getNumber11():
    assert ru.getNumber(15,5) == 11

def test_getNomenclature11():
    assert ru.getNomenclature(15,5) == 'Room 11'

def test_isHallRoomNameTrue():
    assert ru.isHall(roomName='Room 1')
    assert ru.isHall(roomName='Room 2')
    assert ru.isHall(roomName='Room 3')
    assert ru.isHall(roomName='Room 4')

def test_isHallRoomNameFalse():
    assert not ru.isHall(roomName='Room 5')
    assert not ru.isHall(roomName='Room 6')
    assert not ru.isHall(roomName='Room 7')
    assert not ru.isHall(roomName='Room 8')
    assert not ru.isHall(roomName='Room 9')
    assert not ru.isHall(roomName='Room 10')
    assert not ru.isHall(roomName='Room 11')
    assert not ru.isHall(roomName='Room 12')
    assert not ru.isHall(roomName='Room 13')
    assert not ru.isHall(roomName='Room 14')

def test_isHallRoomNameInvalid():
    assert not ru.isHall(roomName='Room -5')
    assert not ru.isHall(roomName='Room 0')
    assert not ru.isHall(roomName='Room 1000')
    assert not ru.isHall(roomName='This is not a room')
    assert not ru.isHall(roomName='41 mooR')
    assert not ru.isHall(roomName='42 42')

def test_isHallRoomNumberTrue():
    assert ru.isHall(roomNumber=1)
    assert ru.isHall(roomNumber=2)
    assert ru.isHall(roomNumber=3)
    assert ru.isHall(roomNumber=4)

def test_isHallRoomNumberFalse():
    assert not ru.isHall(roomNumber=5)
    assert not ru.isHall(roomNumber=6)
    assert not ru.isHall(roomNumber=7)
    assert not ru.isHall(roomNumber=8)
    assert not ru.isHall(roomNumber=9)
    assert not ru.isHall(roomNumber=10)
    assert not ru.isHall(roomNumber=11)
    assert not ru.isHall(roomNumber=12)
    assert not ru.isHall(roomNumber=13)
    assert not ru.isHall(roomNumber=14)

def test_isHallRoomNumberInvalid():
    assert not ru.isHall(roomNumber=0)
    assert not ru.isHall(roomNumber=-15)
    assert not ru.isHall(roomNumber=42)
    assert not ru.isHall(roomNumber=100)
    assert not ru.isHall(roomNumber=10.5)
    assert not ru.isHall(roomNumber=11)
    assert not ru.isHall(roomNumber=12)
    assert not ru.isHall(roomNumber=13)
    assert not ru.isHall(roomNumber=14)

def test_isHallRoomInvalidArguments():
    try:
        ru.isHall()
        ru.isHall(-1, '')
        ru.isHall(-1, None)
    except Exception as e:
        assert True

