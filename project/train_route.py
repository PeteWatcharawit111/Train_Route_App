import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_node import * 
from collections import deque

class TrainRoute:

	def __init__(self):
		self.data_matrix = []
		self.tree_node = TreeNode()
		self.distances = set()
		self.previous_nodes = set()

	def read_csv_file(self, csv_file):
		print("read_csv_file")
		with open(csv_file, 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				if len(words) == 3 and self.is_int(words[2]):
					self.data_matrix.append(words)
				else:
					raise ValueError("file format is not correct, each row should be for example: A,B,5")
		#print(self.data_matrix)

	def is_int(self, nr):
		try:
			int(nr)
			return True
		except:
			return False

	def create_distances(self, node_names):
		#print(node_names)
		self.distances = {node_name: float('inf') for node_name in node_names}
		#print(self.distances)

	def create_previous_nodes(self, node_names):
		#print(node_names)
		self.previous_nodes = {node_name: None for node_name in node_names}
		#print(self.previous_nodes)

	def dijkstra(self, start_station, end_station):
		print("dijkstra")
		#print("self.tree_node: ", self.tree_node)
		#print("self.tree_node.node_names: ", self.tree_node.node_names)
		#print("self.distances: ", self.distances)
		#print("self.previous_nodes: ", self.previous_nodes)

		self.distances[start_station] = 0
		node_names = self.tree_node.node_names.copy()

		while node_names:
			current_node_name = min(node_names, key=lambda node: self.distances[node])
			print("current_node_name: ", current_node_name)
			node_names.remove(current_node_name)
			if self.distances[current_node_name] == float('inf'):
				break
			index = self.tree_node.find_existed_node_name(current_node_name)
			print("index: ", index)
			current_node = self.tree_node.retrieve_node(index)
			print("current_node: ", current_node)
			if current_node:
				for child, cost in current_node.child_list:
					print("child: ", child)
					print("cost: ", cost)
					print("self.distances[current_node_name]:", self.distances[current_node_name])
					alternative_route = self.distances[current_node_name] + int(cost)
					print("alternative_route: ", alternative_route)
					if alternative_route < self.distances[child]:
						self.distances[child] = alternative_route
						self.previous_nodes[child] = current_node_name
			print("***********************")
		path, current_node_name = deque(), end_station
		# check if the path to the destiny is reachable. Otherwise the algorithm warns that it fails
		#print("self.previous_nodes[current_node_name]:", self.previous_nodes[current_node_name])
		try:
			# filling in the dequeue for the path
			while self.previous_nodes[current_node_name] is not None:
				path.appendleft(current_node_name)
				current_node_name = self.previous_nodes[current_node_name]
			if path:
				path.appendleft(current_node_name)
				return [path, self.distances[end_station], len(path) - 2]
			else:
				return "Failed1!"
		except:
			return "Failed2!"
				
	def analyze_route(self):
		print("What station are you getting on the train?:")
		station_from = str(input())
		print("What station are you getting off the train?:")
		station_to = str(input())
		result = self.dijkstra(station_from, station_to)
		print(result)

	



