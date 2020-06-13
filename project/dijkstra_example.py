from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
    #print("make_edge")
    edge = Edge(start, end, cost)
    #print(edge)
    return edge


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        #print("__init__")
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        #for edge in edges:
            #print("edge:", edge)
        self.edges = [make_edge(*edge) for edge in edges]
        #print("self.edges: ", self.edges)

    @property
    def vertices(self):
        #print("vertices")
        vertice_set = set(sum(([edge.start, edge.end] for edge in self.edges), []))
        #print(vertice_set)
        return vertice_set

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        #print("neighbours")
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            #print(edge)
            neighbours[edge.start].add((edge.end, edge.cost))
        #print(neighbours)
        return neighbours

    def dijkstra(self, source, dest):
        #assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        #print("distances: ", distances)
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        #print("previous_vertices: ", previous_vertices)
        distances[source] = 0
        vertices = self.vertices.copy()
        print("vertices:", vertices)
        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                print("here")
                break
            print("current_vertex: " + current_vertex)
            for neighbour, cost in self.neighbours[current_vertex]:
                print("self.neighbours: ", self.neighbours)
                print(self.neighbours[current_vertex])
                #print("neighbour: " + neighbour)
                #print("distances[current_vertex]:", distances[current_vertex])
                print("cost: ", cost)
                print("distances[current_vertex]", distances[current_vertex])
                alternative_route = distances[current_vertex] + cost
                print("alternative_route: ", alternative_route)
                #print("distance[neighbour]: ", distances[neighbour])
                if alternative_route < distances[neighbour]:
                    #print("if")
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex
                    #print("previous_vertices: ", previous_vertices)
            print("*****************************")

        path, current_vertex = deque(), dest
        print("current_vertex: ", current_vertex)
        # check if the path to the destiny is reachable. Otherwise the algorithm warns that it fails
        try:
            print("previous_vertices: ", previous_vertices[current_vertex])
            print("distances:", distances[dest])
            # filling in the dequeue for the path
            while previous_vertices[current_vertex] is not None:
                path.appendleft(current_vertex)
                print("path: ", path)
                current_vertex = previous_vertices[current_vertex]
                print("current_vertex: ", current_vertex)
            if path:
                path.appendleft(current_vertex)
            return [path, distances[dest], len(path) - 2]
        except:
            return "Failed!"


#graph = Graph([
#    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
#    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
#    ("f", "e", 9)])

graph2 = Graph([
    ("A","B",5), ("A","C",7), ("B","D",8), ("D","J",6), ("D","K",6), 
    ("B","E",5), ("B","F",4), ("E","L",8), ("C","I",12), ("C","H",5),
    ("H","M",6), ("I","N",11), ("L","O", 15), ("M","N",6), ("N","O",4),
    ("O","P",5)])

#graph3 = Graph([
#    ("A","B", 5), ("B","C",5), ("C","D",7), ("A","D",15), ("E","F",5),
#    ("F","G", 5), ("G","H",10), ("H","I",10), ("I","J",5), ("G","J",20)
#    ])

print(graph2.dijkstra("A", "N"))