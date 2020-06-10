import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tree_node import *

class TestTreeNode(unittest.TestCase):

	def setUp(self):
		print("setUp")
		self.data_matrix = []
		with open('../routes2.csv', 'r') as f:
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
		bl = tree.node_already_exist(node1)
		
		self.assertFalse(bl)
		
		tree.append_node(node1)
		bl2 = tree.node_already_exist(node1)
		
		self.assertTrue(bl2)
		
		node2 = Node("B")
		tree.append_node(node2)
		bl3 = tree.node_already_exist(node1)
		bl4 = tree.node_already_exist(node2)
		bl5 = tree.node_already_exist(Node("C"))

		self.assertTrue(bl3)
		self.assertTrue(bl4)
		self.assertFalse(bl5)

		node3 = Node("C")
		tree.append_node(node3)
		bl6 = tree.node_already_exist(node3)
		self.assertTrue(bl6)

	def test_find_existed_node(self):
		print("test_find_existed_node")
		tree = TreeNode(self.data_matrix)
		node1 = Node("G")
		index = tree.find_existed_node(node1)
		self.assertEqual(index, -1)

		tree.append_node(node1)
		index = tree.find_existed_node(node1)
		self.assertEqual(index, 0)

		node2 = Node("F")
		tree.append_node(node2)
		index = tree.find_existed_node(node2)
		self.assertEqual(index, 1)

	def test_create_node_tree(self):
		print("test_create_node_tree")
		tree = TreeNode(self.data_matrix)
		tree.create_node_tree(self.data_matrix)
		



if __name__ == '__main__':
	unittest.main()