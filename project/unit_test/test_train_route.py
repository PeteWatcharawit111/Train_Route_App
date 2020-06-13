import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from train_route import *

class TestTrainRoute(unittest.TestCase):

	def setUp(self):
		print("setUp")
		self.data_matrix = []
		with open('../routes2.csv', 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				self.data_matrix.append(words)
		self.tree = TreeNode()
		self.tree.create_node_tree(self.data_matrix)
		self.tree.create_node_names(self.data_matrix)

	def test_init(self):
		print("test_init")
		train_route = TrainRoute()
		self.assertEqual(train_route.data_matrix, [])
		self.assertTrue(isinstance(train_route.tree_node, TreeNode))

	def test_read_csv_file(self):
		print("test_read_csv_file")
		train_route = TrainRoute()
		train_route.read_csv_file("../routes2.csv")
		self.assertTrue(len(train_route.data_matrix) != 0)

	def test_print_queue(self):
		print("test_print_queue")
		train_route = TrainRoute()
		train_route.read_csv_file("../routes2.csv")
		train_route.queue.append(Node("A"))
		train_route.queue.append(Node("K"))
		train_route.print_queue()

	def test_create_distances(self):
		print("test_create_distances")
		train_route = TrainRoute()
		train_route.read_csv_file("../routes2.csv")
		train_route.create_distances(self.tree.node_names)
		self.assertTrue(len(train_route.distances) > 0)
		for name in train_route.distances:
			self.assertEqual(train_route.distances[name], float('inf'))
			
	def test_dijkstra(self):
		print("test_dijkstra")
		train_route = TrainRoute()
		train_route.read_csv_file("../routes2.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.dijkstra("A","N")

if __name__ == '__main__':
	unittest.main()