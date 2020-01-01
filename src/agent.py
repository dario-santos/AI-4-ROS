#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2019-20
# Modified by: 34218 Paulo Silva, 39973 Dário Santos

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import time
import graph_util
import room_util
import Room
import RoomObject

room_ant = 'Room 1'
x_ant = 0
y_ant = 0

obj_ant = ''
G = None
rooms = None
time_initial = time.time()

# ---------------------------------------------------------------
# odometry callback
def callback(data):
	global x_ant, y_ant, room_ant, G, rooms
	
	x = data.pose.pose.position.x
	y = data.pose.pose.position.y

	if room_ant != 'Room -1' and room_util.getNomenclature(x ,y) != 'Room -1':
		room_current = room_util.getNomenclature(x ,y)
		if room_ant != room_current:
			# Localização
			graph_util.addNode(G, room_ant)
			graph_util.addNode(G, room_current)
			graph_util.addEdge(G, room_current, room_ant)

			# Memória
			if not room_util.isHall(roomName=room_ant) and not room_util.isHall(roomName=room_current):
				rooms[room_ant].SetConnectedTo(room_current)
				rooms[room_current].SetConnectedTo(room_ant)
			
			room_ant = room_current

	x_ant = x
	y_ant = y

# ---------------------------------------------------------------
# object_recognition callback
def callback1(data):
	global obj_ant, rooms, room_ant
	obj = data.data

	if obj != obj_ant and data.data != "":
		current_room = rooms[room_ant]

		# Tratar dos dados
		objects= data.data.split(',')
		for _,o in enumerate(objects):
			current_room.AddObject(o)
		
		rooms[room_ant] = current_room
		
	obj_ant = obj
		
# ---------------------------------------------------------------
# questions_keyboard callback
def callback2(data):
	global G, x_ant, y_ant, rooms, time_initial
	
	if data.data == '1':
		cnt = 0
		for key, room in enumerate(rooms.values()):
			if room.IsOccupied():
				cnt += 1

		print "There are %d rooms occupied" % cnt
	if data.data == '2':
		l = []
		for i in G:
			if rooms[i].GetRoomType() == Room.RoomType.suite:
				if rooms[i].GetConnectedTo() not in l:
					l.append(i)
					
		print "There are %d suits" % len(l)

	if data.data == '3':
		print room_util.getProbabilityOfFindingPerson(G, rooms)
	if data.data == '4':
		print room_util.getProbabilityComputer(G, rooms)
	if data.data == '5':
		print graph_util.closestRoom(G, rooms, room_util.getNomenclature(x_ant, y_ant))
	if data.data == '6':
		print graph_util.shortestPath(G, room_util.getNomenclature(x_ant, y_ant))
	if data.data == '7':
		time_diff = time.time() - time_initial 
		numOfBooks = room_util.getNumberOfBooks(rooms)
		estimation = (120 * numOfBooks) / time_diff
		if estimation == 1:
			print "It's estimated that %d book will be found in the next 2 minutes." % estimation
		else:
			print "It's estimated that %d books will be found in the next 2 minutes." % estimation

	if data.data == '9':
		print room_util.getProbabilityOfBeingOccupied(G, rooms)

# ---------------------------------------------------------------
def agent():
	global G, room_ant, rooms

	rospy.init_node('agent')

	rospy.Subscriber("questions_keyboard", String, callback2)
	rospy.Subscriber("object_recognition", String, callback1)
	rospy.Subscriber("odom", Odometry, callback)
	
	# Create graph
	G = graph_util.createGraph()
	graph_util.addNode(G, room_ant)

	# Create dictionary
	rooms = {'Room 1': Room.Room([]),
			 'Room 2': Room.Room([]),
			 'Room 3': Room.Room([]),
			 'Room 4': Room.Room([]),
			 'Room 5': Room.Room([]),
			 'Room 6': Room.Room([]),
			 'Room 7': Room.Room([]),
			 'Room 8': Room.Room([]),
			 'Room 9': Room.Room([]),
			 'Room 10': Room.Room([]),
			 'Room 11': Room.Room([]),
			 'Room 12': Room.Room([]),
			 'Room 13': Room.Room([]),
			 'Room 14': Room.Room([])
			 }

	rospy.spin()

# ---------------------------------------------------------------
if __name__ == '__main__':
	agent()
