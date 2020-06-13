import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_node import * 

class TrainRoute:

	def __init__(self):
		self.data_matrix = []
		self.tree_node = TreeNode()

	def read_csv_file(self, csv_file):
		print("read_csv_file")
		with open(csv_file, 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				self.data_matrix.append(words)
		#print(self.data_matrix)

	def dijkstra(self, start_station, end_station):
		print("dijkstra")
		print(self.tree_node)

		# find the start_station in the tree
		start_index = self.tree_node.find_existed_node_name(start_station)
		start_node = self.tree_node.retrieve_node(start_index)
		#print(start_node)

		# find the end_station in the tree
		end_index = self.tree_node.find_existed_node_name(end_station)
		end_node = self.tree_node.retrieve_node(end_index)
		#print(end_node)

				
	def analyze_route(self):
		print("What station are you getting on the train?:")
		station_from = str(input())
		print("What station are you getting off the train?:")
		station_to = str(input())

if __name__ == '__main__':
	train_route = TrainRoute()
	train_route.read_csv_file("routes.csv")

	station_tree = TreeNode(train_route.data_matrix)
	#print(station_tree)

	



