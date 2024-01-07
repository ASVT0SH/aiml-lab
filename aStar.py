def a_star_algorithm(start_node, goal_node):

    open_set = set([start_node])
    closed_set = set()
    distance_from_start = {}  # store distance from starting node
    parent_nodes = {}  # parent_nodes contain an adjacency map of all nodes
    # distance of starting node from itself is zero
    distance_from_start[start_node] = 0
    # start_node is the root node i.e. it has no parent nodes
    # so start_node is set to its own parent node
    parent_nodes[start_node] = start_node

    while len(open_set) > 0:
        current_node = None
        # node with the lowest f() is found
        for node in open_set:
            if current_node is None or distance_from_start[node] + heuristic(node) < distance_from_start[current_node] + heuristic(current_node):
                current_node = node

        if current_node == goal_node or Graph_neighbors[current_node] is None:
            pass
        else:
            for (neighbor, weight) in get_neighbors(current_node):
                # neighbors 'neighbor' not in the open_set and closed_set are added to the open_set
                # current_node is set to its parent
                if neighbor not in open_set and neighbor not in closed_set:
                    open_set.add(neighbor)
                    parent_nodes[neighbor] = current_node
                    distance_from_start[neighbor] = distance_from_start[current_node] + weight
                # for each node neighbor, compare its distance from start i.e distance_from_start(neighbor)
                # to the distance_from_start through current_node
                else:
                    if distance_from_start[neighbor] > distance_from_start[current_node] + weight:
                        # update distance_from_start(neighbor)
                        distance_from_start[neighbor] = distance_from_start[current_node] + weight
                        # change the parent of neighbor to current_node
                        parent_nodes[neighbor] = current_node
                        # if neighbor in closed set, remove and add to open_set
                        if neighbor in closed_set:
                            closed_set.remove(neighbor)
                            open_set.add(neighbor)

        if current_node is None:
            print('Path does not exist!')
            return None

        # if the current node is the goal_node
        # then we begin reconstructing the path from it to the start_node
        if current_node == goal_node:
            path = []
            while parent_nodes[current_node] != current_node:
                path.append(current_node)
                current_node = parent_nodes[current_node]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # remove current_node from the open_set, and add it to the closed_set
        # because all of its neighbors were inspected
        open_set.remove(current_node)
        closed_set.add(current_node)

    print('Path does not exist!')
    return None

# define function to return neighbor and its distance
# from the passed node
def get_neighbors(node):
    if node in Graph_neighbors:
        return Graph_neighbors[node]
    else:
        return None

# for simplicity, we'll consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(node):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[node]

# Describe your graph here
Graph_neighbors = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

a_star_algorithm('A', 'G')
