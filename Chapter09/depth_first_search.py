
graph = dict()  
graph['A'] = ['B', 'S']  
graph['B'] = ['A']  
graph['S'] = ['A', 'G', 'C']  
graph['D'] = ['C']  
graph['G'] = ['S', 'F', 'H']  
graph['H'] = ['G', 'E']  
graph['E'] = ['C', 'H']  
graph['F'] = ['C', 'G']  
graph['C'] = ['D', 'S', 'E', 'F']  

def depth_first_search(graph, root): 
    visited_vertices = list()  # List to keep track of visited nodes
    graph_stack = list()  # Stack for DFS
    graph_stack.append(root)  # Push the root node onto the stack
    node = root  # Start from the root node

    while graph_stack: 
        if node not in visited_vertices: 
            visited_vertices.append(node)  # Mark the node as visited
        adj_nodes = graph[node]  # Get all adjacent nodes of the current node

        if set(adj_nodes).issubset(set(visited_vertices)): 
            graph_stack.pop()  # Pop the node from the stack if all adjacent nodes are visited
            if len(graph_stack) > 0: 
                node = graph_stack[-1]  # Set the current node to the top of the stack
            continue 
        else: 
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))  # Get unvisited adjacent nodes
            
        first_adj_node = sorted(remaining_elements)[0]  # Get the first unvisited adjacent node
        graph_stack.append(first_adj_node)  # Push the node onto the stack
        node = first_adj_node  # Set the current node to the first adjacent node

    return visited_vertices  # Return the list of visited nodes

print(depth_first_search(graph, 'A'))  # Perform DFS starting from node 'A'
####################################################################################################

# ### Time and Space Complexities

# - **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges. This is because each vertex and edge is processed once.
# - **Space Complexity:** O(V), where V is the number of vertices. This is due to the space required to store the visited vertices and the stack.

# ### Visual Representation

# 1. **Initial Graph:**
#    ```
#        A
#       / \
#      B   S
#         / \
#        G   C
#       /|   |\
#      F H   E D
#         \ / 
#          H
#    ```

# 2. **DFS Traversal Order from 'A':**
#    - Start from 'A'
#    - Visit 'B'
#    - Backtrack to 'A'
#    - Visit 'S'
#    - Visit 'C'
#    - Visit 'D'
#    - Backtrack to 'C'
#    - Visit 'E'
#    - Backtrack to 'C'
#    - Visit 'F'
#    - Backtrack to 'S'
#    - Visit 'G'
#    - Visit 'H'

#    ```
#    A -> B -> S -> C -> D -> E -> F -> G -> H
#    ```

# ### Step-by-Step Visual Representation

# 1. **Start at Node 'A'**
#    ```
#    Visited: [A]
#    Stack: [A]
#    ```

# 2. **Visit 'A', Push 'B', 'S'**
#    ```
#    Visited: [A, B]
#    Stack: [A, B]
#    ```

# 3. **Visit 'B' (No new nodes), Backtrack to 'A'**
#    ```
#    Visited: [A, B]
#    Stack: [A]
#    ```

# 4. **Visit 'S', Push 'G', 'C'**
#    ```
#    Visited: [A, B, S]
#    Stack: [A, S]
#    ```

# 5. **Visit 'C', Push 'D', 'E', 'F'**
#    ```
#    Visited: [A, B, S, C]
#    Stack: [A, S, C]
#    ```

# 6. **Visit 'D' (No new nodes), Backtrack to 'C'**
#    ```
#    Visited: [A, B, S, C, D]
#    Stack: [A, S, C]
#    ```

# 7. **Visit 'E' (No new nodes), Backtrack to 'C'**
#    ```
#    Visited: [A, B, S, C, D, E]
#    Stack: [A, S, C]
#    ```

# 8. **Visit 'F' (No new nodes), Backtrack to 'S'**
#    ```
#    Visited: [A, B, S, C, D, E, F]
#    Stack: [A, S]
#    ```

# 9. **Visit 'G', Push 'H'**
#    ```
#    Visited: [A, B, S, C, D, E, F, G]
#    Stack: [A, S, G]
#    ```

# 10. **Visit 'H' (No new nodes)**
#     ```
#     Visited: [A, B, S, C, D, E, F, G, H]
#     Stack: [A, S, G, H]
#     ```

# ### Use Cases and Explanation

# 1. **Path Finding:**
#    - **Why:** DFS explores as far as possible along each branch before backtracking.
#    - **For What:** Useful for finding paths in mazes, puzzles, and games.

# 2. **Topological Sorting:**
#    - **Why:** DFS can be used to order vertices in a directed acyclic graph (DAG).
#    - **For What:** Useful in scheduling tasks, resolving dependencies, and organizing data.

# 3. **Cycle Detection:**
#    - **Why:** DFS can detect cycles in both directed and undirected graphs.
#    - **For What:** Useful in detecting deadlocks in operating systems and circular dependencies in software.

# 4. **Connected Components:**
#    - **Why:** DFS can be used to explore all nodes in a connected component.
#    - **For What:** Identifying connected components in a graph, such as in network analysis.

# 5. **Solving Puzzles:**
#    - **Why:** DFS can explore all possible moves in puzzles.
#    - **For What:** Useful in solving puzzles like Sudoku, crosswords, and word searches.

# ### Summary

# Depth-first search (DFS) is a fundamental graph traversal algorithm that explores nodes as far as possible along each branch before backtracking. It is widely used in various applications, including path finding, topological sorting, cycle detection, identifying connected components, and solving puzzles.

# If you have any more questions or need further clarification, feel free to ask!

# Source: Conversation with Copilot, 9/1/2024
# (1) github.com. https://github.com/byron-hai/PythonOn/tree/0fe48b124e13eb3cff89e3cbd31b0d144f67c3d7/data_structure%2Fgraph%2Fgraph_traversal.py.
# (2) github.com. https://github.com/tsaoalbert/test.tensor.flow/tree/a0b04c1c92ca51f5474cf0a037b97d6b22378e14/others%2Fmy.361%2Fbackup%2FChapter08%2Fdfs_graph.py.