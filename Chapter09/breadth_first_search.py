
graph = dict()  
graph['A'] = ['B', 'G', 'D']  
graph['B'] = ['A', 'F', 'E']  
graph['C'] = ['F', 'H']  
graph['D'] = ['F', 'A']  
graph['E'] = ['B', 'G']  
graph['F'] = ['B', 'D', 'C']  
graph['G'] = ['A', 'E']  
graph['H'] = ['C']  

# Graph Representation:
# A -- B -- E
# |    |    |
# G -- F -- C -- H
# |    |
# D -- F

from collections import deque

def breadth_first_search(graph, root): 
    visited_vertices = list()  # List to keep track of visited nodes
    graph_queue = deque([root])  # Queue for BFS
    visited_vertices.append(root)  # Mark the root as visited
    node = root  # Start from the root node

    while len(graph_queue) > 0: 
        node = graph_queue.popleft()  # Dequeue a node from the front of the queue
        adj_nodes = graph[node]  # Get all adjacent nodes of the dequeued node

        remaining_elements = set(adj_nodes).difference(set(visited_vertices))  # Get unvisited adjacent nodes
        if len(remaining_elements) > 0: 
            for elem in sorted(remaining_elements):  # Sort to maintain consistent order
                visited_vertices.append(elem)  # Mark the node as visited
                graph_queue.append(elem)  # Enqueue the node

    return visited_vertices  # Return the list of visited nodes

print(breadth_first_search(graph, 'A'))  # Perform BFS starting from node 'A'


# ### Time and Space Complexities

# - **Time Complexity:** O(V + E), where V is the number of vertices and E is the number of edges. This is because each vertex and edge is processed once.
# - **Space Complexity:** O(V), where V is the number of vertices. This is due to the space required to store the visited vertices and the queue.

# ### Visual Representation

# 1. **Initial Graph:**
#    ```
#    A -- B -- E
#    |    |    |
#    G -- F -- C -- H
#    |    |
#    D -- F
#    ```

# 2. **BFS Traversal Order from 'A':**
#    - Start from 'A'
#    - Visit 'B', 'D', 'G'
#    - Visit 'E', 'F'
#    - Visit 'C'
#    - Visit 'H'

#    ```
#    A -> B -> D -> G -> E -> F -> C -> H
#    ```

# ### Use Cases and Explanation

# 1. **Shortest Path in Unweighted Graphs:**
#    - **Why:** BFS explores all nodes at the present depth level before moving on to nodes at the next depth level.
#    - **For What:** Finding the shortest path in unweighted graphs, such as in social networks or road maps.

# 2. **Level Order Traversal in Trees:**
#    - **Why:** BFS can be used to traverse a tree level by level.
#    - **For What:** Useful in scenarios like printing a tree level by level or finding the level of a node in a tree.

# 3. **Connected Components:**
#    - **Why:** BFS can be used to explore all nodes in a connected component.
#    - **For What:** Identifying connected components in a graph, such as in network analysis.

# 4. **Cycle Detection in Undirected Graphs:**
#    - **Why:** BFS can help detect cycles by keeping track of visited nodes.
#    - **For What:** Detecting cycles in undirected graphs, which is useful in various applications like dependency resolution.

# 5. **Web Crawlers:**
#    - **Why:** BFS can be used to explore web pages level by level.
#    - **For What:** Web crawlers use BFS to index web pages by exploring links from a starting page.

# ### Summary

# Breadth-first search (BFS) is a fundamental graph traversal algorithm that explores nodes level by level. It is widely used in various applications, including finding the shortest path in unweighted graphs, level order traversal in trees, identifying connected components, cycle detection, and web crawling.


# ### Initial Graph Representation

# ```
#     A
#    /|\
#   B G D
#   | | |
#   F E F
#   |   |
#   C   C
#   |   |
#   H   H
# ```

# ### BFS Traversal from Node 'A'

# 1. **Start at Node 'A'**
#    - Queue: [A]
#    - Visited: [A]

# 2. **Visit Node 'A' and Enqueue its Neighbors (B, G, D)**
#    - Queue: [B, G, D]
#    - Visited: [A, B, G, D]

# 3. **Visit Node 'B' and Enqueue its Neighbors (F, E)**
#    - Queue: [G, D, F, E]
#    - Visited: [A, B, G, D, F, E]

# 4. **Visit Node 'G' (All Neighbors Already Visited)**
#    - Queue: [D, F, E]
#    - Visited: [A, B, G, D, F, E]

# 5. **Visit Node 'D' (All Neighbors Already Visited)**
#    - Queue: [F, E]
#    - Visited: [A, B, G, D, F, E]

# 6. **Visit Node 'F' and Enqueue its Neighbor (C)**
#    - Queue: [E, C]
#    - Visited: [A, B, G, D, F, E, C]

# 7. **Visit Node 'E' (All Neighbors Already Visited)**
#    - Queue: [C]
#    - Visited: [A, B, G, D, F, E, C]

# 8. **Visit Node 'C' and Enqueue its Neighbor (H)**
#    - Queue: [H]
#    - Visited: [A, B, G, D, F, E, C, H]

# 9. **Visit Node 'H' (All Neighbors Already Visited)**
#    - Queue: []
#    - Visited: [A, B, G, D, F, E, C, H]

# ### Final BFS Traversal Order

# ```
# A -> B -> G -> D -> F -> E -> C -> H
# ```

# ### Step-by-Step Visual Representation

# 1. **Start at Node 'A'**
#    ```
#    Visited: [A]
#    Queue: [A]
#    ```

# 2. **Visit 'A', Enqueue 'B', 'G', 'D'**
#    ```
#    Visited: [A, B, G, D]
#    Queue: [B, G, D]
#    ```

# 3. **Visit 'B', Enqueue 'F', 'E'**
#    ```
#    Visited: [A, B, G, D, F, E]
#    Queue: [G, D, F, E]
#    ```

# 4. **Visit 'G' (No new nodes)**
#    ```
#    Visited: [A, B, G, D, F, E]
#    Queue: [D, F, E]
#    ```

# 5. **Visit 'D' (No new nodes)**
#    ```
#    Visited: [A, B, G, D, F, E]
#    Queue: [F, E]
#    ```

# 6. **Visit 'F', Enqueue 'C'**
#    ```
#    Visited: [A, B, G, D, F, E, C]
#    Queue: [E, C]
#    ```

# 7. **Visit 'E' (No new nodes)**
#    ```
#    Visited: [A, B, G, D, F, E, C]
#    Queue: [C]
#    ```

# 8. **Visit 'C', Enqueue 'H'**
#    ```
#    Visited: [A, B, G, D, F, E, C, H]
#    Queue: [H]
#    ```

# 9. **Visit 'H' (No new nodes)**
#    ```
#    Visited: [A, B, G, D, F, E, C, H]
#    Queue: []
#    ```

# ### Summary

# The BFS traversal starts from node 'A' and explores all its neighbors before moving on to the next level of nodes. This ensures that nodes are visited in the order of their distance from the starting node.

# If you have any more questions or need further clarification, feel free to ask!