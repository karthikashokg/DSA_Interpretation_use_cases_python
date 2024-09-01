
# Define the graph using an adjacency list
graph = dict() 
graph['A'] = ['B', 'C'] 
graph['B'] = ['E', 'C', 'A'] 
graph['C'] = ['A', 'B', 'E', 'F'] 
graph['E'] = ['B', 'C'] 
graph['F'] = ['C']

# Get the sorted list of vertices
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)  # Number of rows and columns in the adjacency matrix

# Initialize the adjacency matrix with zeros
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)] 

# Initialize the list to store edges
edges_list = [] 

# Create a list of edges from the adjacency list
for key in matrix_elements: 
    for neighbor in graph[key]: 
        edges_list.append((key, neighbor)) 

print(edges_list)  # Print the list of edges

# Fill the adjacency matrix based on the edges list
for edge in edges_list: 
    index_of_first_vertex = matrix_elements.index(edge[0]) 
    index_of_second_vertex = matrix_elements.index(edge[1]) 
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1 

print(adjacency_matrix)  # Print the adjacency matrix
###########################################################

### Time and Space Complexities

# - **Time Complexity:**
#   - Creating the edges list: O(V + E), where V is the number of vertices and E is the number of edges.
#   - Filling the adjacency matrix: O(E), where E is the number of edges.
#   - Overall: O(V + E).

# - **Space Complexity:**
#   - Adjacency matrix: O(V^2), where V is the number of vertices.
#   - Edges list: O(E), where E is the number of edges.
#   - Overall: O(V^2).

# ### Visual Representation

# 1. **Initial Graph:**
#    ```
#        A
#       / \
#      B   C
#     /|   |\
#    E C   E F
#    ```

# 2. **Edges List:**
#    ```
#    [('A', 'B'), ('A', 'C'), ('B', 'E'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B'), ('C', 'E'), ('C', 'F'), ('E', 'B'), ('E', 'C'), ('F', 'C')]
#    ```

# 3. **Adjacency Matrix:**
#    ```
#    A B C E F
#    A 0 1 1 0 0
#    B 1 0 1 1 0
#    C 1 1 0 1 1
#    E 0 1 1 0 0
#    F 0 0 1 0 0
#    ```

# ### Use Cases and Explanation

# 1. **Graph Representation:**
#    - **Why:** Adjacency matrices provide a straightforward way to represent graphs.
#    - **For What:** Useful in algorithms that require quick access to check if an edge exists between two vertices.

# 2. **Graph Algorithms:**
#    - **Why:** Many graph algorithms, such as Floyd-Warshall for shortest paths, use adjacency matrices.
#    - **For What:** Useful in applications like network routing, social network analysis, and molecular biology.

# 3. **Dense Graphs:**
#    - **Why:** Adjacency matrices are efficient for dense graphs where the number of edges is close to the number of vertices squared.
#    - **For What:** Suitable for applications where the graph is dense, such as in certain types of simulations and modeling.

# 4. **Matrix Operations:**
#    - **Why:** Adjacency matrices allow the use of matrix operations to perform graph computations.
#    - **For What:** Useful in scientific computing and engineering applications where matrix operations are common.

# ### Summary

# Creating an adjacency matrix from a graph provides a clear and efficient way to represent the graph, especially for dense graphs. It allows for quick access to check the existence of edges and is useful in various graph algorithms and applications.

# If you have any more questions or need further clarification, feel free to ask!

# Source: Conversation with Copilot, 9/1/2024
# (1) github.com. https://github.com/Saurabh919yadav/HandsOn-Python-Notes/tree/b3665327bf52750faeba3ea1912043f9a4792a48/Graphs%2FGraph.py.
# (2) github.com. https://github.com/andriitugai/Learning-Python-data-structures/tree/f9225e150bda7eeb3ba38f29c134c1a643b76302/Chapter08%2Fgraph.py.
# (3) github.com. https://github.com/sashadev-sky/ADT-Guide/tree/99dc1e36d7f336f94ee0ca2f5ff81f44a62dfa3b/python%2Fgraph.py.
# (4) github.com. https://github.com/ramchinta/Algorithms/tree/08c4b8d216a43ac8a2c0297d3083ba4b0a806e22/Graphs.py.
# (5) github.com. https://github.com/apachecn/apachecn-python-zh/tree/63de9c961cf62843fb4361128e2f7cc30c7457fa/trans%2Fget-start-py%2F11.md.