To run the application do:

1) from /project, in terminal run ex. : python main.py --file=./input_files/routes.csv


To run the unit tests do:

1) from /unit_test, in terminal run: python -m unittest for all test suits or python -m unittest test_node.py, alternatively run: python test_node.py
2) to run a specific test case ex. : python test_train_route.py TestTrainRoute.test_dijkstra4 

TODO for the improvement of the project

1) Tweak the algorithm so that it returns the path with the least number of stops when there are two equal distance paths between start_station to end_station.

2) In case we want to implement two-way train stations, we would need to provide the reversed path of A,B,5 which is B,A,5 as well.

3) If the program has to call the algorithm a few times, some variables must be cleansed after each run to avoid bugs preferably with a method purge().

4) create a Dockerfile for this application!

References:

https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
