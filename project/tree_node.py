from node import *

class TreeNode():

	def __init__(self, data_matrix):
		self.tree = []

	def create_node_tree(self, data_matrix):
		#print("hello")
		for i in range(len(data_matrix)):
			node = Node(data_matrix[i][0])
			child_data = [ data_matrix[i][1], data_matrix[i][2] ]
			node.add_child(child_data)
			if not self.node_already_exist(node):
				self.append_node(node)
			else:
				#print("already in the tree work on adding it's child")
				#print(node)
				index = self.find_existed_node(node)
				#print(index)
				child_data = [ data_matrix[i][1], data_matrix[i][2] ]
				self.tree[index].add_child(child_data)
				
		print(self)

	def node_already_exist(self, n):
		exist = False
		for i in range(len(self.tree)):
			if n.node == self.tree[i].node:
				exist = True
		return exist

	def find_existed_node(self, n):
		index = -1
		for i in range(len(self.tree)):
			if n.node == self.tree[i].node:
				index = i
		return index

	def append_node(self, n):
		self.tree.append(n)

	def __str__(self):
		for node in self.tree:
			print(node)
		return ""

