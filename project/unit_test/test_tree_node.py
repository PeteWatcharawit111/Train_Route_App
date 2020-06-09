import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_node import *

class TestTreeNode(unittest.TestCase):

	def setUp(self):
		print("setUp")
		self.data_matrix = []
		with open('../routes.csv', 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				self.data_matrix.append(words)

	def test_init(self):
		print("test_init")
		tree = TreeNode(self.data_matrix)

	def test_append_node(self):
		print("test_append_node")
		tree = TreeNode(self.data_matrix)
		node = Node("A")
		tree.append_node(node)
		self.assertTrue(len(tree.tree) == 1)
		node = Node("B")
		tree.append_node(node)
		self.assertTrue(len(tree.tree) == 2)

	def test_node_already_exist(self):
		print("test_node_already_exist")
		tree = TreeNode(self.data_matrix)
		node1 = Node("A")
		tree.append_node(node1)
		node2 = Node("B")
		tree.append_node(node2)
		print(tree)

if __name__ == '__main__':
	unittest.main()