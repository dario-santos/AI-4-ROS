import pytest
import dependencies
import sys 
sys.path.insert(0, dependencies.program_path)

from src import RoomObject as rObject

def test_objectCategories():
    o1 = rObject.RoomObject(rObject.Category.person, "Anna")
    o2 = rObject.RoomObject(rObject.Category.door, "door1")
    o3 = rObject.RoomObject(rObject.Category.bed, "bed1")
    o4 = rObject.RoomObject(rObject.Category.book, "book1")
    o5 = rObject.RoomObject(rObject.Category.chair, "chair1")
    o6 = rObject.RoomObject(rObject.Category.computer, "windows xp")
    o7 = rObject.RoomObject(rObject.Category.table, "table1")
    o8 = rObject.RoomObject(rObject.Category.mistery, "what is this")

    assert o1.GetCategory() == rObject.Category.person
    assert o2.GetCategory() == rObject.Category.door
    assert o3.GetCategory() == rObject.Category.bed
    assert o4.GetCategory() == rObject.Category.book
    assert o5.GetCategory() == rObject.Category.chair
    assert o6.GetCategory() == rObject.Category.computer
    assert o7.GetCategory() == rObject.Category.table
    assert o8.GetCategory() == rObject.Category.mistery

def test_objectName():
    o1 = rObject.RoomObject(rObject.Category.person, 'Anna')
    assert o1.GetName() == 'Anna'
    o1.SetName('Maria')
    assert o1.GetName() == 'Maria'

def test_objectCategory():
    o1 = rObject.RoomObject(rObject.Category.person, "Anna")
    assert o1.GetCategory() == rObject.Category.person
    o1.SetCategory(rObject.Category.mistery)
    assert o1.GetCategory() == rObject.Category.mistery
        
