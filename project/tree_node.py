from node import *

class TreeNode():

	def __init__(self, data_matrix):
		self.tree = []
		#print(data_matrix)
		
		#for i in range(len(data_matrix)):
		#	node = Node(data_matrix[i][0])
		#	child_data = [ data_matrix[i][1], data_matrix[i][2] ]
		#	node.add_child(child_data)
		#	self.tree.append(node)
		#print(self)

	def node_already_exist(self):
		print("hello")
		for node in self.tree:
			print(node)




	def append_node(self, n):
		self.tree.append(n)

	def __str__(self):
		for node in self.tree:
			print(node)
		return ""

