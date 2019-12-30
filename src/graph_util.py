import networkx as nx
import room_util
import Room

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
	
	if currentPos == 'Room -1':
	 return "Please move a little, you are between two rooms."

	try: 
		path = nx.astar_path(G, currentPos, goalPos, weight='weight')
	except Exception as e:
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

def closestRoom(G, rooms, current_room):
	if current_room == 'Room -1':
	 return "Please move a little bit, you are between two rooms."

	dic = nx.algorithms.shortest_path(G, current_room, weight='weight')
	closestRoom = None
	smallestPath = 999

	for _,k in enumerate(dic.keys()):
		if k == current_room:
			continue

		if (len(dic[k]) < smallestPath) and rooms[k].GetRoomType() == Room.RoomType.single:
			smallestPath = len(dic[k])
			closestRoom = k

	if closestRoom is None:
		return "No known single rooms"

	return "The room %s is the closest single room." % closestRoom
