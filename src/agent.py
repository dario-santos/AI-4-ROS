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
	global x_ant, y_ant, room_ant, G, rooms
	
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y

	if room_ant != 'Room -1' and room_util.getNomenclature(x ,y) != 'Room -1':
		room_current = room_util.getNomenclature(x ,y)
		if room_ant != room_current:
			# Localização
			graph_util.addNode(G, room_ant)
			graph_util.addNode(G, room_current)
			graph_util.addEdge(G, room_current, room_ant)

			# Memória
			if not room_util.isHall(roomName=room_ant) and not room_util.isHall(roomName=room_current):
				rooms[room_ant].SetIsSuit(True)
				rooms[room_current].SetIsSuit(True)
			
			room_ant = room_current

			
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
	global G, x_ant, y_ant, rooms
	
	if data.data == '1':
		cnt = 0
		for _,room in enumerate(rooms.values()): 
			if room.IsOccupied():
				cnt += 1
		print "There are %d rooms occupied" % cnt
	if data.data == '2':
		cnt = 0
		for _,room in enumerate(rooms.values()): 
			if room.GetIsSuit():
				cnt += 1
		cnt /= 2
		print "There are %d suits" % cnt
	if data.data == '3':
		print room_util.getProbabilityOfBeingOccupied(G, rooms)
	
	if data.data == '4':
		
		count_single = 0
		count_double = 0
		count_suite = 0
		count_meeting = 0
		count_generic = 0
		count_pc_single = 0.0
		count_pc_double = 0.0
		count_pc_suite = 0.0
		count_pc_meeting = 0.0
		count_pc_generic = 0.0
		prob_single = 0.0
		prob_double = 0.0
		prob_suite = 0.0
		prob_meeting = 0.0
		prob_generic = 0.0
		
		for _, room in enumerate(rooms.values()):
			if room.GetRoomType() == Room.RoomType.single:
				count_single += 1
				if len(room.GetObjectsByCategory(RoomObject.Category.computer)) != 0:
					count_pc_single += 1
				
			elif room.GetRoomType() == Room.RoomType.double:
				if len(room.GetObjectsByCategory(RoomObject.Category.computer)) != 0:
					 count_double += 1
					 count_pc_double += 1
				else:
					count_double += 1 
					
			elif room.GetRoomType() == Room.RoomType.suite:
				if len(room.GetObjectsByCategory(RoomObject.Category.computer)) != 0:
					count_suite += 1 
					count_pc_suite += 1
				else:
					count_suite += 1
					
			elif room.GetRoomType() == Room.RoomType.meeting:
				if len(room.GetObjectsByCategory(RoomObject.Category.computer)) != 0:
					count_meeting += 1 
					count_pc_meeting += 1
				else:
					count_meeting += 1
					
			elif room.GetRoomType() == Room.RoomType.generic:
				count_generic += 1

				if len(room.GetObjectsByCategory(RoomObject.Category.computer)) > 0:
					count_pc_generic += 1
					
		if count_single != 0:
			prob_single = count_pc_single / count_single
		if count_double != 0:
			prob_double = count_pc_double / count_double
		if count_suite != 0:
			prob_suite = count_pc_suite / count_suite
		if count_meeting != 0:
			prob_meeting = count_pc_meeting / count_meeting
		if count_generic != 0:
			prob_generic = count_pc_generic / count_generic
		
		l = [prob_single, prob_double, prob_suite, prob_meeting, prob_generic]

		max = 0.0
		index = 0
		for i,p in enumerate(l):
			if p > max:
				max = p
				index = i
		
		print "MAIOR PROBABILIDADE %f , no indice %d" % (max, index)
		
		if prob_single > prob_double and prob_single > prob_suite and prob_single > prob_meeting and prob_single > prob_generic:
			probSi = prob_single * 100
			print "The probability of finding a computer is higher in the single room and is (%.0f%%)" % probSi
		
		elif prob_double > prob_suite and prob_double > prob_meeting and prob_double > prob_generic:
			probD = prob_double * 100
			print "The probability of finding a computer is higher in the suite room and is (%0.f%%)" % probD
		
		elif prob_suite > prob_meeting and prob_suite > prob_generic:
			probSu = prob_suite *100
			print "The probability of finding a computer is higher in the meeting room and is(%0.f%%)" % probSu
		
		elif prob_meeting > prob_generic:
			probM = prob_meeting *100
			print "The probability of finding a computer is higher in the meeting room and is(%0.f%%)" % probM
		
		elif prob_generic != 0.0:
			probG = prob_generic * 100
			print "The probability of finding a computer is higher in the generic room and is(%0.f%%)" % probG
		else:
			print "No computers found yet."
	
	if data.data == '5':
		print graph_util.closestRoom(G, rooms, room_util.getNomenclature(x_ant, y_ant))
		
	if data.data == '6':
		print graph_util.shortestPath(G, room_util.getNomenclature(x_ant, y_ant))

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
