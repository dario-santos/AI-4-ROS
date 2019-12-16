import pytest
import sys
sys.path.insert(1, '../')

from src import RoomObject as rObject
from src import Room as r

def test_Room():
    r1 = r.Room([])
    assert r1.objects == []
    r1.AddObject("person_Maria")
    assert r1.objects[0].GetCategory() == rObject.Category.person

def test_duplicateItems():
    r1 = r.Room([])
    assert len(r1.objects) == 0
    r1.AddObject("person_Maria")
    r1.AddObject("person_Maria")
    assert len(r1.objects) == 1

def test_roomIsSingle():
    r1 = r.Room([])
    r1.AddObject("bed_bed1")
    assert r1.GetRoomType() == 'single room'

def test_roomIsDouble():
    r1 = r.Room([])
    r1.AddObject("bed_bed1")
    r1.AddObject("bed_bed2")
    assert r1.GetRoomType() == 'double room'

def test_roomIsSuite():
    r1 = r.Room([])
    r1.SetIsSuit(True)
    r1.AddObject("bed_bed1")
    r1.AddObject("bed_bed2")
    assert r1.GetRoomType() == 'suite'

def test_roomIsMeeting():
    r1 = r.Room([])
    r1.AddObject("table_table1")
    r1.AddObject("chair_chair1")
    r1.AddObject("chair_chair2")
    r1.AddObject("chair_chair3")
    assert r1.GetRoomType() == 'meeting room'

def test_roomIsGeneric():
    r1 = r.Room([])
    r1.AddObject("table_table1")
    r1.AddObject("chair_chair1")
    r1.AddObject("chair_chair2")
    r1.AddObject("book_book2")
    assert r1.GetRoomType() == 'generic room'
