import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from train_route import *

class TestTrainRoute(unittest.TestCase):

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

	def test_BFS(self):
		print("test_BFS")
		train_route = TrainRoute()
		train_route.read_csv_file("../routes2.csv")
		train_route.tree_node.create_node_tree(train_route.data_matrix)
		train_route.BFS("A","N")

if __name__ == '__main__':
	unittest.main()