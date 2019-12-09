#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2019-20
# Modified by: Students names and numbers

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
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

# ---------------------------------------------------------------
# odometry callback
def callback(data):
	global x_ant, y_ant, room_ant, G
	
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y

	if room_ant != 'Room -1' and room_util.GetNomenclature(x ,y) != 'Room -1':
		if room_ant != room_util.GetNomenclature(x ,y):
			graph_util.addNode(G, room_ant)
			graph_util.addNode(G, room_util.GetNomenclature(x, y))
			graph_util.addEdge(G, room_util.GetNomenclature(x, y), room_ant)
			room_ant = room_util.GetNomenclature(x, y)


	# show coordinates only when they change
	if x != x_ant or y != y_ant:
		print " x=%.1f y=%.1f" % (x,y)
		print room_ant

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
			print "object is %s" % o
		
		rooms[room_ant] = current_room
		print "object is %s" % data.data
		
	obj_ant = obj
		
# ---------------------------------------------------------------
# questions_keyboard callback
def callback2(data):
	global G, x_ant, y_ant, rooms, room_ant

	if data.data == '1':
		if rooms[room_ant].IsOccupied():
			print "This room is occupied"
		else: 
			print "This room is not occupied"

	if data.data == '5':
		print graph_util.closestRoom(G, room_util.GetNomenclature(x_ant, y_ant))
	if data.data == '6':
		print graph_util.shortestPath(G, room_util.GetNomenclature(x_ant, y_ant))

	print "question is %s" % data.data

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
