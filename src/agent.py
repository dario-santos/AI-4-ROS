#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2019-20
# Modified by: Students names and numbers

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

import room_util
import Room
import networkx as nx
import matplotlib.pyplot as plt
import csv

x_ant = 0
y_ant = 0
obj_ant = ''
G = None

#----------------------------------------------------------------
# Declare Graph
def createGraph(filepath='/home/viki/catkin_ws/src/ia/src/salas.txt'):
	G = nx.Graph()

	with open(filepath, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		
		for row in spamreader:
			if row[0] not in nx.classes.function.nodes(G):
				G.add_node(row[0])
			if row[1] not in nx.classes.function.nodes(G):
				G.add_node(row[1])
			G.add_edge(row[0], row[1], weight= int(row[2]))
	return G

#------------------------------------------------------------------
# Shortest path to elevator
def shortestPath(G, currentPos, goalPos='S1'):
	formatedPath = ''
	path = nx.astar_path(G, currentPos, goalPos, weight='weight')
	
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

# ---------------------------------------------------------------
# odometry callback
def callback(data):
	global x_ant, y_ant
	x=data.pose.pose.position.x
	y=data.pose.pose.position.y
	# show coordinates only when they change
	if x != x_ant or y != y_ant:
		print " x=%.1f y=%.1f" % (x,y)
		print room_util.IsHall(room_util.GetNumber(x,y))
	x_ant = x
	y_ant = y

# ---------------------------------------------------------------
# object_recognition callback
def callback1(data):
	global obj_ant
	obj = data.data
	if obj != obj_ant and data.data != "":
		print "object is %s" % data.data
	obj_ant = obj
		
# ---------------------------------------------------------------
# questions_keyboard callback
def callback2(data):
	global G, x_ant, y_ant 

	if data.data == "6":
		print shortestPath(G, room_util.GetNomenclature(x_ant, y_ant))

	print "question is %s" % data.data

# ---------------------------------------------------------------
def agent():
	global G

	rospy.init_node('agent')

	rospy.Subscriber("questions_keyboard", String, callback2)
	rospy.Subscriber("object_recognition", String, callback1)
	rospy.Subscriber("odom", Odometry, callback)
	
	G = createGraph()
	# nx.draw(G, with_labels='trye')
	# plt.show()

	rospy.spin()

# ---------------------------------------------------------------
if __name__ == '__main__':
	agent()
