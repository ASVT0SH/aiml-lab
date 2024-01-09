class Graph:
    def __init__(self, graph, heuristicNodeList, startNode):
        # Instantiate graph object with graph topology, heuristic values, and start node
        self.graph = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}

    def apply_ao_star(self):
        # Start a recursive AO* algorithm
        self.aoStar(self.start, False)

    def getNeighbors(self, v):
        # Get the neighbors of a given node
        return self.graph.get(v, '')

    def getStatus(self, v):
        # Return the status of a given node
        return self.status.get(v, 0)

    def setStatus(self, v, val):
        # Set the status of a given node
        self.status[v] = val

    def getHeuristicNodeValue(self, n):
        # Return the heuristic value of a given node
        return self.H.get(n, 0)

    def setHeuristicNodeValue(self, n, value):
        # Set the revised heuristic value of a given node
        self.H[n] = value

    def print_solution(self):
        # Print the solution graph
        print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
        print("------------------------------------------------------------")
        print(self.solutionGraph)
        print("------------------------------------------------------------")

    def computeMinimumCostChildNodes(self, v):
        # Computes the Minimum Cost of child nodes of a given node v
        minimumCost = 0
        costToChildNodeListDict = {}
        costToChildNodeListDict[minimumCost] = []
        flag = True

        for nodeInfoTupleList in self.getNeighbors(v):
            cost = 0
            nodeList = []

            for c, weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)

            if flag:
                minimumCost = cost
                costToChildNodeListDict[minimumCost] = nodeList
                flag = False
            else:
                if minimumCost > cost:
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList

        return minimumCost, costToChildNodeListDict[minimumCost]

    def aoStar(self, v, backTracking):
        # AO* algorithm for a start node and backTracking status flag
        print("HEURISTIC VALUES :", self.H)
        print("SOLUTION GRAPH :", self.solutionGraph)
        print("PROCESSING NODE :", v)
        print("-----------------------------------------------------------------------------------------")

        if self.getStatus(v) >= 0:
            # If status node v >= 0, compute Minimum Cost nodes of v
            minimumCost, childNodeList = self.computeMinimumCostChildNodes(v)
            self.setHeuristicNodeValue(v, minimumCost)
            self.setStatus(v, len(childNodeList))

            solved = True
            # Check the Minimum Cost nodes of v are solved
            for childNode in childNodeList:
                self.parent[childNode] = v
                if self.getStatus(childNode) != -1:
                    solved = solved and False

            if solved:
                # If the Minimum Cost nodes of v are solved, set the current node status as solved(-1)
                self.setStatus(v, -1)
                # Update the solution graph with the solved nodes, which may be a part of the solution
                self.solutionGraph[v] = childNodeList

            if v != self.start:
                # Check if the current node is the start node for backtracking the current node value
                self.aoStar(self.parent[v], True)

            if not backTracking:
                # Check if the current call is not for backtracking
                for childNode in childNodeList:
                    # For each Minimum Cost child node
                    self.setStatus(childNode, 0)
                    # Set the status of child node to 0 (needs exploration)
                    self.aoStar(childNode, False)


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
