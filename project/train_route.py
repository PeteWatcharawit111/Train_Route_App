import os
import sys
import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_node import * 
from collections import deque

class TrainRoute:
	"""TrainRoute class contains the read file method and methods for the chosen algorithm to analyze the path and distance."""
	def __init__(self):
		self.data_matrix = []
		self.tree_node = TreeNode()
		self.distances = set()
		self.previous_nodes = set()

	def read_csv_file(self, csv_file):
		with open(csv_file, 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				if len(words) == 3 and self.is_positive_int(words[2]):
					self.data_matrix.append(words)
				else:
					raise ValueError("file format is not correct, each row should be for example: A,B,5")
		#print(self.data_matrix)

	def two_way_route(self):
		two_way_matrix = copy.deepcopy(self.data_matrix)
		for i in range(len(two_way_matrix)):
			two_way_matrix[i][0], two_way_matrix[i][1] = two_way_matrix[i][1], two_way_matrix[i][0]
			self.data_matrix.append(two_way_matrix[i])

	def is_positive_int(self, nr):
		try:
			number = int(nr)
			if(number >= 0):
				return True
			else:
				return False
		except:
			return False

	def create_distances(self, node_names):
		self.distances = {node_name: float('inf') for node_name in node_names}

	def create_previous_nodes(self, node_names):
		self.previous_nodes = {node_name: None for node_name in node_names}

	def check_station_exist(self, station):
		existed = False
		for node_name in self.tree_node.node_names:
			if station == node_name:
				existed = True
				break
		return existed

	def dijkstra(self, start_station, end_station):

		self.distances[start_station] = 0
		node_names = self.tree_node.node_names.copy()

		while node_names:
			current_node_name = min(node_names, key=lambda node: self.distances[node])
			node_names.remove(current_node_name)
			if self.distances[current_node_name] == float('inf'):
				break
			index = self.tree_node.find_existed_node_name(current_node_name)
			current_node = self.tree_node.retrieve_node(index)
			if current_node:
				for child, cost in current_node.child_list:
					alternative_route = self.distances[current_node_name] + int(cost)
					if alternative_route < self.distances[child]:
						self.distances[child] = alternative_route
						self.previous_nodes[child] = current_node_name
		path, current_node_name = deque(), end_station
		# filling in the dequeue for the path
		while self.previous_nodes[current_node_name] is not None:
			path.appendleft(current_node_name)
			current_node_name = self.previous_nodes[current_node_name]
		if path:
			path.appendleft(current_node_name)
			result = [path, self.distances[end_station], len(path) - 2]
			#print(result)
			return "Your trip from " + start_station + " to " + end_station + " includes " + str(result[2]) + " stops and will take " + str(result[1]) + " minutes"
			
		else:
			return "No routes from " + start_station + " to " + end_station

	def analyze_route(self):
		print("What station are you getting on the train?:")
		station_from = str(input())
		if not self.check_station_exist(station_from):
			sys.exit("start station not found")
		
		print("What station are you getting off the train?:")
		station_to = str(input())
		if not self.check_station_exist(station_to):
			sys.exit("end station not found")

		if station_from == station_to:
			sys.exit("the start and end station are the same!")
				
		result_msg = self.dijkstra(station_from, station_to)
		print(result_msg)
		

	



