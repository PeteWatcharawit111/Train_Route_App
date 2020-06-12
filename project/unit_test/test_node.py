import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from node import *

class TestNode(unittest.TestCase):

	def test_init(self):
		print("test_init")
		node = Node("A")
		self.assertEqual(node.node, "A")
		self.assertEqual(node.child_list, [])
		self.assertEqual(node.visited, False)
		self.assertEqual(node.parent_list, [])

	def test_add_child(self):
		print("test_add_child")
		node = Node("B")
		child_data = ["C","5"]
		node.add_child(child_data)
		self.assertEqual(node.node, "B")
		self.assertEqual(node.child_list, [child_data])

		node = Node("C")
		child_data = ["D","7"]
		node.add_child(child_data)
		self.assertEqual(node.node, "C")
		self.assertEqual(node.child_list, [child_data])
		child_data2 = ["G","8"]
		node.add_child(child_data2)
		self.assertEqual(node.child_list, [child_data, child_data2])

	def test_add_parent(self):
		print("test_add_parent")
		node = Node("F")
		parent_data = ["B", "4"]
		node.add_parent(parent_data)
		self.assertEqual(node.node, "F")
		self.assertEqual(node.parent_list, [parent_data])

	def test_is_equal(self):
		print("test_is_equal")
		node = Node("A")
		node2 = Node("B")
		node3 = Node("B")
		bl = node.is_equal(node2)
		self.assertFalse(bl)
		bl = node2.is_equal(node3)
		self.assertTrue(bl)

if __name__ == '__main__':
	unittest.main()



