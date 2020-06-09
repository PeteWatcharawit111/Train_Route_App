

class Node:
	"""Node class is a basic class that represents train stations as different nodes"""
	def __init__(self, n):
		self.node = n
		self.child_list = []

	def add_child(self, child_data):
		#print("add_child")
		self.child_list.append(child_data)

	def is_equal(self, n):
		bl = False
		if self.node == n.node:
			bl = True
		return bl

	def __str__(self):
		ret_string = str(self.node) + ": " + str(self.child_list)
		return ret_string