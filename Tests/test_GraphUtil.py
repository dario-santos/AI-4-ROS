import pytest
import sys

sys.path.insert(1, 'C:\\Users\\dario\\OneDrive\\Documentos\\Github\\IA-4-ROS\\')

from src import graph_util as g

def test_createGraph():
    G = g.createGraph()
    assert G != None 

def test_addNode():
    G = g.createGraph()
    g.addNode(G, 'Room 1')
    assert G.has_node('Room 1')

def test_addSameNodes():
    G = g.createGraph()
    assert len(list(G.nodes)) == 0
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1

def test_addInvalidNode():
    G = g.createGraph()
    assert len(list(G.nodes)) == 0
    g.addNode(G, 'Room -1')
    assert len(list(G.nodes)) == 0

def test_addTwoNode():
    G = g.createGraph()
    assert len(list(G.nodes)) == 0
    g.addNode(G, 'Room 1')
    assert len(list(G.nodes)) == 1
    g.addNode(G, 'Room 2')
    assert len(list(G.nodes)) == 2

def test_addEdge():
    G = g.createGraph()
    assert len(list(G.edges)) == 0
    
    g.addNode(G, 'Room 1')
    g.addNode(G, 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 1


def test_addEdgeToEmptyGraph():
    G = g.createGraph()
    assert len(list(G.edges)) == 0
    
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 0

def test_addEdgeInvalidNode1():
    G = g.createGraph()
    assert len(list(G.edges)) == 0
    g.addNode(G, 'Room 2')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 0

def test_addEdgeInvalidNode2():
    G = g.createGraph()
    assert len(list(G.edges)) == 0
    g.addNode(G, 'Room 1')
    g.addEdge(G, 'Room 1', 'Room 2')
    assert len(list(G.edges)) == 0

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
    assert len(list(G.edges)) == 0