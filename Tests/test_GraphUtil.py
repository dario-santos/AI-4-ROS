import pytest
import dependencies 
import sys
sys.path.insert(0, dependencies.program_path)

from src import graph_util as g

def test_createGraph():
    G = g.createGraph()
    assert G is not None 

def test_addNode():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    assert G.has_node('Room 1')

def test_addSameNodes():
    G = g.createGraph()
    assert not list(G.nodes)
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1

def test_addInvalidNode():
    G = g.createGraph()
    assert not list(G.nodes)
    g.addNode(G, 'Room -1')
    assert not list(G.nodes)

def test_addTwoNode():
    G = g.createGraph()
    assert not list(G.nodes)
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1
    g.addNode(G, 'Room 2')
    assert len(list(G.nodes)) == 2

def test_addEdge():
    G = g.createGraph()
    assert not list(G.edges)
    
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 1


def test_addEdgeToEmptyGraph():
    G = g.createGraph()
    assert not list(G.edges)
    
    g.addEdge(G, 'Room 1', 'Room 2')
    assert not list(G.edges)

def test_addEdgeInvalidNode1():
    G = g.createGraph()
    assert not list(G.edges)
    g.addNode(G, 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert not list(G.edges)

def test_addEdgeInvalidNode2():
    G = g.createGraph()
    assert not list(G.edges)
    g.addNode(G, 'Room 1')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert not list(G.edges)

def test_addDuplicateEdge():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 1

def test_addEdgeInvalidNodes():
    G = g.createGraph()
    g.addNode(G, 'Room -1')
    g.addNode(G, 'Room -2')
    g.addEdge(G, 'Room -1', 'Room -2')
    assert not list(G.edges)


def test_shortestPath():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    g.addNode(G, 'Room 3')
    g.addNode(G, 'Room 4')
    g.addEdge(G, 'Room 1', 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 3')
    g.addEdge(G, 'Room 2', 'Room 4')
    g.addEdge(G, 'Room 3', 'Room 2')
    assert g.shortestPath(G, 'Room 4') == "Room 4 -> Room 2 -> Room 1"

def test_shortestPathSameRoom():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    assert g.shortestPath(G, 'Room 1') == "Room 1"

def test_shortestPathNoConnection():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    assert g.shortestPath(G, 'Room 2') == "There is no possible connection to Room 1 from Room 2"

def test_shortestPathNoConnection():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    assert g.shortestPath(G, 'Room 2') == "There is no possible connection to Room 1 from Room 2"

def test_shortestPathInvalidRoomOrigin():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room -1')
    g.addEdge(G, 'Room 1', 'Room -1')
    assert g.shortestPath(G, 'Room -1') == "Please move a little, you are between two rooms."
