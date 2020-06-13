

class Node:
	"""Node class is a basic class that represents train stations as different nodes"""
	def __init__(self, n):
		self.name = n
		self.child_list = []
		self.visited = False 

	def add_child(self, child_data):
		self.child_list.append(child_data)

	def is_equal(self, n):
		bl = False
		if self.name == n.name:
			bl = True
		return bl

	def __str__(self):
		ret_string = str(self.name) + ": " + "visited: " + str(self.visited) + " Child: " + str(self.child_list)
		return ret_string