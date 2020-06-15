import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from train_route import *

class TestTrainRoute(unittest.TestCase):

	def setUp(self):
		print("setUp")
		self.data_matrix = []
		with open('../input_files/routes2.csv', 'r') as f:
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
		train_route.read_csv_file("../input_files/routes2.csv")
		self.assertTrue(len(train_route.data_matrix) != 0)

	def test_is_positive_int(self):
		print("test_is_positive_int")
		train_route = TrainRoute()
		self.assertFalse(train_route.is_positive_int("a"))
		self.assertFalse(train_route.is_positive_int("a0"))
		self.assertTrue(train_route.is_positive_int("0"))
		self.assertTrue(train_route.is_positive_int("23"))
		self.assertFalse(train_route.is_positive_int("-2"))

	def test_create_distances(self):
		print("test_create_distances")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.create_distances(self.tree.node_names)
		self.assertTrue(len(train_route.distances) > 0)
		for name in train_route.distances:
			self.assertEqual(train_route.distances[name], float('inf'))

	def test_create_previous_nodes(self):
		print("test_create_previous_nodes")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.create_previous_nodes(self.tree.node_names)
		self.assertTrue(len(train_route.previous_nodes) > 0)
		for name in train_route.previous_nodes:
			self.assertEqual(train_route.previous_nodes[name], None)

	def test_check_station_exist(self):
		print("test_check_station_exist")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.tree_node.create_node_names(train_route.data_matrix)
		bl1 = train_route.check_station_exist("A")
		self.assertTrue(bl1)
		bl2 = train_route.check_station_exist("a")
		self.assertFalse(bl2)
		bl3 = train_route.check_station_exist("C")
		self.assertTrue(bl3)
		bl4 = train_route.check_station_exist("c")
		self.assertFalse(bl4)
		bl5 = train_route.check_station_exist("1")
		self.assertFalse(bl5)

	def test_dijkstra(self):
		print("test_dijkstra")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.tree_node.create_node_names(train_route.data_matrix)
		train_route.create_distances(train_route.tree_node.node_names)
		train_route.create_previous_nodes(train_route.tree_node.node_names)
		result_msg = train_route.dijkstra("A","B")
		msg = "Your trip from A to B includes 0 stops and will take 5 minutes"
		self.assertTrue(result_msg, msg)

	def test_dijkstra2(self):
		print("test_dijkstra2")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.tree_node.create_node_names(train_route.data_matrix)
		train_route.create_distances(train_route.tree_node.node_names)
		train_route.create_previous_nodes(train_route.tree_node.node_names)
		result_msg = train_route.dijkstra("A","N")
		msg = "Your trip from A to N includes 3 stops and will take 24 minutes"
		self.assertTrue(result_msg, msg)

	def test_dijkstra3(self):
		print("test_dijkstra3")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes2.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.tree_node.create_node_names(train_route.data_matrix)
		train_route.create_distances(train_route.tree_node.node_names)
		train_route.create_previous_nodes(train_route.tree_node.node_names)
		result_msg = train_route.dijkstra("B","N")
		msg = "No routes from B to N"
		self.assertTrue(result_msg, msg)

	def test_dijkstra4(self):
		print("test_dijkstra4")
		train_route = TrainRoute()
		train_route.read_csv_file("../input_files/routes3.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.tree_node.create_node_names(train_route.data_matrix)
		train_route.create_distances(train_route.tree_node.node_names)
		train_route.create_previous_nodes(train_route.tree_node.node_names)
		result_msg = train_route.dijkstra("a","e")
		msg = "Your trip from a to e includes 2 stops and will take 20 minutes"
		self.assertTrue(result_msg, msg)

if __name__ == '__main__':
	unittest.main()