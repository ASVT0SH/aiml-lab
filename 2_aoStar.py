class Graph:
    def __init__(self, adjacency_list, heuristic_values, start_node):
        # Instantiate a graph object with the graph topology, heuristic values, and start node
        self.adjacency_list = adjacency_list
        self.heuristic_values = heuristic_values
        self.start_node = start_node
        self.parent_nodes = {}
        self.node_status = {}
        self.solution_graph = {}

    def apply_ao_star(self):
        # Start the recursive AO* algorithm
        self.ao_star(self.start_node, False)

    def get_neighbors(self, node):
        # Get the neighbors of a given node
        return self.adjacency_list.get(node, [])

    def get_node_status(self, node):
        # Return the status of a given node
        return self.node_status.get(node, 0)

    def set_node_status(self, node, value):
        # Set the status of a given node
        self.node_status[node] = value

    def get_heuristic_value(self, node):
        # Return the heuristic value of a given node
        return self.heuristic_values.get(node, 0)

    def set_heuristic_value(self, node, value):
        # Set the revised heuristic value of a given node
        self.heuristic_values[node] = value

    def print_solution(self):
        # Print the solution graph
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start_node)
        print("------------------------------------------------------------")
        print(self.solution_graph)
        print("------------------------------------------------------------")

    def compute_minimum_cost_child_nodes(self, node):
        # Computes the Minimum Cost of child nodes of a given node
        minimum_cost = 0
        cost_to_child_node_list_dict = {minimum_cost: []}
        flag = True

        for neighbors_list in self.get_neighbors(node):
            cost = 0
            node_list = []

            for child_node, weight in neighbors_list:
                cost += self.get_heuristic_value(child_node) + weight
                node_list.append(child_node)

            if flag:
                minimum_cost = cost
                cost_to_child_node_list_dict[minimum_cost] = node_list
                flag = False
            else:
                if minimum_cost > cost:
                    minimum_cost = cost
                    cost_to_child_node_list_dict[minimum_cost] = node_list

        return minimum_cost, cost_to_child_node_list_dict[minimum_cost]

    def ao_star(self, node, back_tracking):
        # AO* algorithm for a start node and backtracking status flag
        print("HEURISTIC VALUES:", self.heuristic_values)
        print("SOLUTION GRAPH:", self.solution_graph)
        print("PROCESSING NODE:", node)
        print("-----------------------------------------------------------------------------------------")

        if self.get_node_status(node) >= 0:
            minimum_cost, child_node_list = self.compute_minimum_cost_child_nodes(node)
            self.set_heuristic_value(node, minimum_cost)
            self.set_node_status(node, len(child_node_list))

            solved = True
            for child_node in child_node_list:
                self.parent_nodes[child_node] = node
                if self.get_node_status(child_node) != -1:
                    solved = solved and False

            if solved:
                self.set_node_status(node, -1)
                self.solution_graph[node] = child_node_list

            if node != self.start_node and back_tracking:
                self.ao_star(self.parent_nodes[node], True)

            if not back_tracking:
                for child_node in child_node_list:
                    self.set_node_status(child_node, 0)
                    self.ao_star(child_node, False)

h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
graph1 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'C': [[('J', 1)]],
    'D': [[('E', 1), ('F', 1)]],
    'G': [[('I', 1)]]
}
g1 = Graph(graph1, h1, 'A')
g1.apply_ao_star()
g1.print_solution()

h2 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
graph2 = {
    'A': [[('B', 1), ('C', 1)], [('D', 1)]],
    'B': [[('G', 1)], [('H', 1)]],
    'D': [[('E', 1), ('F', 1)]]
}

g2 = Graph(graph2, h2, 'A')
g2.apply_ao_star()
g2.print_solution()
