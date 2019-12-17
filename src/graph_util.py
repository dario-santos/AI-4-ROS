import networkx as nx
#import matplotlib.pyplot as plt

from src import room_util

def createGraph():
	G = nx.Graph()
	return G


def addNode(G, node):
	if G.has_node(node):
		return
	if node == room_util.room_nomenclature_prefix + '-1':
		return

	G.add_node(node)


def addEdge(G, node_1, node_2):
	if (not G.has_node(node_1)) or (not G.has_node(node_2)):
		return
	if G.has_edge(node_1, node_2):
		return
	if node_1 == node_2:
		return
	if node_1 == room_util.room_nomenclature_prefix + '-1' or node_2 == room_util.room_nomenclature_prefix + '-1':
		return
	
	G.add_edge(node_1, node_2, weigth=1)


def shortestPath(G, currentPos, goalPos='Room 1'):
	formatedPath = ''
	try: 
		path = nx.astar_path(G, currentPos, goalPos, weight='weight')
	except:
		return "There is no possible connection to " + goalPos + " from " + currentPos

	if len(path) - 1 == 0:
		formatedPath = currentPos
	else: 
		formatedPath = currentPos + " -> "
	
	for i,e in enumerate(path):
		if i == 0:
			continue
		if i == len(path) - 1:
			formatedPath += e
			continue

		formatedPath += e + " -> " 

	return	formatedPath

def closestRoom(G, current_room):
	neighbours = list(G.neighbors(current_room))
	output = "Closest rooms: "
	if len(neighbours) == 0:
		output += "None"
	
	for i,node in enumerate(neighbours):
		if i == len(neighbours) - 1:
			output += node
			continue

		output += node + ", "   
	return output

#def showGraph(G):
#	nx.draw(G, with_labels='true')
#	plt.show()
#	return
