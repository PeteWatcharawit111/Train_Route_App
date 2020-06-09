from tree_node import * 

class TrainRoutes:

	def __init__(self):
		self.data_matrix = []

	def read_csv_file(self, csv_file):
		print("read_csv_file")
		with open('routes.csv', 'r') as f:
			for line in f:
				words = line.rstrip().split(',')
				self.data_matrix.append(words)
		#print(self.data_matrix)
				
	def analyze_route(self):
		print("What station are you getting on the train?:")
		station_from = str(input())
		print("What station are you getting off the train?:")
		station_to = str(input())

if __name__ == '__main__':
	train_route = TrainRoutes()
	train_route.read_csv_file("routes.csv")

	station_tree = TreeNode(train_route.data_matrix)
	#print(station_tree)

	



