
def get_shortest_distance(table, vertex): 
    # Retrieve the shortest distance for the given vertex from the table
    shortest_distance = table[vertex][DISTANCE] 
    return shortest_distance 

def set_shortest_distance(table, vertex, new_distance): 
    # Set the shortest distance for the given vertex in the table
    table[vertex][DISTANCE] = new_distance 

def set_previous_node(table, vertex, previous_node): 
    # Set the previous node for the given vertex in the table
    table[vertex][PREVIOUS_NODE] = previous_node 

def get_distance(graph, first_vertex, second_vertex): 
    # Retrieve the distance between two vertices from the graph
    return graph[first_vertex][second_vertex] 

def get_next_node(table, visited_nodes): 
    # Get the next node to visit based on the shortest distance
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes))) 
    assumed_min = table[unvisited_nodes[0]][DISTANCE] 
    min_vertex = unvisited_nodes[0] 
    for node in unvisited_nodes: 
        if table[node][DISTANCE] < assumed_min: 
            assumed_min = table[node][DISTANCE] 
            min_vertex = node 
    return min_vertex 

def find_shortest_path(graph, table, origin): 
    visited_nodes = []  # List to keep track of visited nodes
    current_node = origin  # Start with the origin node
    starting_node = origin  # Keep track of the starting node

    while True: 
        adjacent_nodes = graph[current_node]  # Get adjacent nodes of the current node
        if set(adjacent_nodes).issubset(set(visited_nodes)): 
            # If all adjacent nodes have been visited, do nothing
            pass 
        else: 
            unvisited_nodes = set(adjacent_nodes).difference(set(visited_nodes)) 
            for vertex in unvisited_nodes: 
                distance_from_starting_node = get_shortest_distance(table, vertex) 
                if distance_from_starting_node == INFINITY and current_node == starting_node: 
                    total_distance = get_distance(graph, vertex, current_node) 
                else: 
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex) 
                if total_distance < distance_from_starting_node: 
                    set_shortest_distance(table, vertex, total_distance) 
                    set_previous_node(table, vertex, current_node) 
        visited_nodes.append(current_node) 
        if len(visited_nodes) == len(table.keys()): 
            break 
        current_node = get_next_node(table, visited_nodes) 
    return table

# Define the graph with distances between nodes
graph = dict() 
graph['A'] = {'B': 5, 'D': 9, 'E': 2} 
graph['B'] = {'A': 5, 'C': 2} 
graph['C'] = {'B': 2, 'D': 3} 
graph['D'] = {'A': 9, 'F': 2, 'C': 3} 
graph['E'] = {'A': 2, 'F': 3} 
graph['F'] = {'E': 3, 'D': 2} 

# Initialize the table with distances and previous nodes
table = { 
    'A': [0, None], 
    'B': [float("inf"), None], 
    'C': [float("inf"), None], 
    'D': [float("inf"), None], 
    'E': [float("inf"), None], 
    'F': [float("inf"), None], 
}

DISTANCE = 0 
PREVIOUS_NODE = 1 
INFINITY = float('inf')  

# Find the shortest path from the origin node 'A'
shortest_distance_table = find_shortest_path(graph, table, 'A') 

# Print the shortest distances from the origin node to all other nodes
for k in sorted(shortest_distance_table): 
    print("{} - {}".format(k, shortest_distance_table[k]))
# ```

# ### Time and Space Complexities

# - **Time Complexity**: The time complexity of Dijkstra's algorithm, which this implementation resembles, is \(O(V^2)\) where \(V\) is the number of vertices. This is because each vertex is processed and the distances to all other vertices are updated.
# - **Space Complexity**: The space complexity is \(O(V)\) for storing the distance table and the visited nodes list.

# ### Interpretation

# This implementation is a variant of Dijkstra's algorithm for finding the shortest path in a weighted graph. Here's a step-by-step interpretation:

# 1. **Initialization**:
#    - The graph is defined with distances between nodes.
#    - The table is initialized with distances set to infinity (`inf`) and previous nodes set to `None`, except for the origin node which has a distance of 0.

# 2. **Main Loop**:
#    - The algorithm iterates until all nodes have been visited.
#    - For each node, it checks the distances to its adjacent nodes.
#    - If a shorter path to an adjacent node is found, the distance and previous node are updated in the table.

# 3. **Get Next Node**:
#    - The next node to visit is selected based on the shortest distance from the origin node that hasn't been visited yet.

# 4. **Update Distances**:
#    - The distances to adjacent nodes are updated based on the current node's distance and the edge weights.

# 5. **Termination**:
#    - The loop terminates when all nodes have been visited.

# 6. **Output**:
#    - The shortest distances from the origin node to all other nodes are printed.

# ### Example

# For the given graph, the algorithm finds the shortest paths from node 'A' to all other nodes. The output will show the shortest distances and the previous nodes for each node.

# Would you like any further details or another example?

# Source: Conversation with Copilot, 9/1/2024
# (1) github.com. https://github.com/apachecn/apachecn-python-zh/tree/63de9c961cf62843fb4361128e2f7cc30c7457fa/trans%2Fhandson-dsal-py%2F13.md.
# (2) github.com. https://github.com/PhilosAccounting/ts-learning/tree/aaf58731f83098212cef2084e143e540c2f46b7f/3_Alg_Data_Structures%2F315-DataStructures%2FHands-On%20Data%20Structures%20and%20Algorithms_Code%2FChapter13%2Fdijkstra.py.
# (3) github.com. https://github.com/ramchinta/Algorithms/tree/08c4b8d216a43ac8a2c0297d3083ba4b0a806e22/DijkstrasShortestPathAlgorithm.py.

# Sure, let's visualize the graph and explain the steps of finding the shortest path using Dijkstra's algorithm. We'll use the given graph structure and show the process step-by-step.

# ### 1. **Initial Graph:**

# ```
#     A
#    / \
#   B   S
#      / \
#     G   C
#    /|   |\
#   F H   E D
#      \ / 
#       H
# ```

# ### 2. **Graph Representation:**

# We'll represent the graph with distances between nodes:

# ```
# graph = {
#     'A': {'B': 5, 'S': 2},
#     'B': {'A': 5, 'C': 4},
#     'S': {'A': 2, 'G': 3, 'C': 6},
#     'G': {'S': 3, 'F': 1, 'H': 4},
#     'C': {'B': 4, 'S': 6, 'E': 2, 'D': 7},
#     'F': {'G': 1},
#     'H': {'G': 4, 'E': 3},
#     'E': {'C': 2, 'H': 3},
#     'D': {'C': 7}
# }
# ```

# ### 3. **Initial Table:**

# The table stores the shortest distances from the origin node 'A' to all other nodes and the previous node in the shortest path.

# ```
# table = {
#     'A': [0, None],
#     'B': [float("inf"), None],
#     'S': [float("inf"), None],
#     'G': [float("inf"), None],
#     'C': [float("inf"), None],
#     'F': [float("inf"), None],
#     'H': [float("inf"), None],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# ### 4. **Step-by-Step Explanation:**

# #### Step 1: Start at Node 'A'

# - Current Node: `A`
# - Adjacent Nodes: `B`, `S`
# - Update distances:
#   - `B`: 5 (via `A`)
#   - `S`: 2 (via `A`)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [float("inf"), None],
#     'C': [float("inf"), None],
#     'F': [float("inf"), None],
#     'H': [float("inf"), None],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# #### Step 2: Move to Node 'S'

# - Current Node: `S`
# - Adjacent Nodes: `A`, `G`, `C`
# - Update distances:
#   - `G`: 5 (via `S`)
#   - `C`: 8 (via `S`)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [float("inf"), None],
#     'H': [float("inf"), None],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# #### Step 3: Move to Node 'B'

# - Current Node: `B`
# - Adjacent Nodes: `A`, `C`
# - Update distances:
#   - `C`: 9 (via `B`) (No update since 8 < 9)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [float("inf"), None],
#     'H': [float("inf"), None],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# #### Step 4: Move to Node 'G'

# - Current Node: `G`
# - Adjacent Nodes: `S`, `F`, `H`
# - Update distances:
#   - `F`: 6 (via `G`)
#   - `H`: 9 (via `G`)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# #### Step 5: Move to Node 'F'

# - Current Node: `F`
# - Adjacent Nodes: `G`
# - No updates needed.

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [float("inf"), None],
#     'D': [float("inf"), None]
# }
# ```

# #### Step 6: Move to Node 'C'

# - Current Node: `C`
# - Adjacent Nodes: `B`, `S`, `E`, `D`
# - Update distances:
#   - `E`: 10 (via `C`)
#   - `D`: 15 (via `C`)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [10, 'C'],
#     'D': [15, 'C']
# }
# ```

# #### Step 7: Move to Node 'H'

# - Current Node: `H`
# - Adjacent Nodes: `G`, `E`
# - Update distances:
#   - `E`: 12 (via `H`) (No update since 10 < 12)

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [10, 'C'],
#     'D': [15, 'C']
# }
# ```

# #### Step 8: Move to Node 'E'

# - Current Node: `E`
# - Adjacent Nodes: `C`, `H`
# - No updates needed.

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [10, 'C'],
#     'D': [15, 'C']
# }
# ```

# #### Step 9: Move to Node 'D'

# - Current Node: `D`
# - Adjacent Nodes: `C`
# - No updates needed.

# ```
# table = {
#     'A': [0, None],
#     'B': [5, 'A'],
#     'S': [2, 'A'],
#     'G': [5, 'S'],
#     'C': [8, 'S'],
#     'F': [6, 'G'],
#     'H': [9, 'G'],
#     'E': [10, 'C'],
#     'D': [15, 'C']
# }
# ```

# ### Final Shortest Distance Table:

# ```
# A - [0, None]
# B - [5, 'A']
# S - [2, 'A']
# G - [5, 'S']
# C - [8, 'S']
# F - [6, 'G']
# H - [9, 'G']
# E - [10, 'C']
# D - [15, 'C']
# ```

# This table shows the shortest distances from the origin node 'A' to all other nodes and the previous node in the shortest path.

# Would you like any further details or another example?