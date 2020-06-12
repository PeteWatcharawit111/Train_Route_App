

class Node:
	"""Node class is a basic class that represents train stations as different nodes"""
	def __init__(self, n):
		self.node = n
		self.child_list = []
		self.visited = False
		self.parent_list = [] 

	def add_child(self, child_data):
		self.child_list.append(child_data)

	def is_equal(self, n):
		bl = False
		if self.node == n.node:
			bl = True
		return bl

	def add_parent(self, parent_data):
		self.parent_list.append(parent_data)

	def __str__(self):
		ret_string = str(self.node) + ": " + "visited: " + str(self.visited) + " " + str(self.child_list)
		if len(self.parent_list) != 0:
			ret_string = str(self.node) + ": " + "visited: " + str(self.visited) + " Parent: " + self.parent_list + " " + str(self.child_list)
		return ret_string