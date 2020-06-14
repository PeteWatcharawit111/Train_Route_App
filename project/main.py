import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from train_route import *



if __name__ == '__main__':
	print("main")
	train_route = TrainRoute()
	if sys.argv[1].startswith("--file=") and sys.argv[1].endswith(".csv"):
		file_name = sys.argv[1][7:]
		train_route.read_csv_file(file_name)
	else:
		sys.exit("Wrong input format, expected: python --file=path/input.csv, example: python --file=./input_files/routes2.csv")
	train_route.tree_node.create_node_tree(train_route.data_matrix)
	train_route.tree_node.create_node_names(train_route.data_matrix)
	train_route.create_distances(train_route.tree_node.node_names)
	train_route.create_previous_nodes(train_route.tree_node.node_names)
	train_route.analyze_route()
