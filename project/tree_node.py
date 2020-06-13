from node import *

class TreeNode():

	def __init__(self):
		self.tree = []
		self.tree_set = set()
		self.node_names = set()

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
				
		#print(self)

	def create_node_tree_set(self, data_matrix):

		print(self.tree_set)
		print(data_matrix)
		print(data_matrix[0])

	def create_node_names(self, data_matrix):
		for data in data_matrix:
			self.node_names.add(data[0])
			self.node_names.add(data[1])

	def node_already_exist(self, n):
		exist = False
		for i in range(len(self.tree)):
			if n.name == self.tree[i].name:
				exist = True
		return exist

	def find_existed_node(self, n):
		index = -1
		for i in range(len(self.tree)):
			if n.name == self.tree[i].name:
				index = i
		return index

	def find_existed_node_name(self, name):
		index = -1
		for i in range(len(self.tree)):
			if name == self.tree[i].name:
				index = i
		return index

	def retrieve_node(self, index):
		try:
			return self.tree[index]
		except IndexError:
			return None

	def append_node(self, n):
		self.tree.append(n)

	def __str__(self):
		for node in self.tree:
			print(node)
		return ""

