class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.elements = []
        # Time Complexity: O(1)
        # Space Complexity: O(1)
        
    def push(self, item):
        # Append an item to the stack
        self.elements.append(item)
        # Time Complexity: O(1)
        # Space Complexity: O(1)
    
    def pop(self):
        # Remove and return the last item from the stack
        return self.elements.pop()
        # Time Complexity: O(1)
        # Space Complexity: O(1)


class TreeNode:
    def __init__(self, data=None):
        # Initialize the tree node with data and set left and right children to None
        self.data = data
        self.right = None
        self.left = None
        # Time Complexity: O(1)
        # Space Complexity: O(1)

def calc(node):
    # Recursively calculate the value of the expression tree
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return node.data
    # Time Complexity: O(n) (where n is the number of nodes in the tree)
    # Space Complexity: O(h) (due to the recursion stack, where h is the height of the tree)

# Expression to be evaluated
expr = "4 5 + 5 3 - *".split()

# Initialize an empty stack
stack = Stack()

# Iterate through each term in the expression
for term in expr:
    if term in "+-*/":
        # If the term is an operator, create a new tree node with the operator
        node = TreeNode(term)
        # Pop two nodes from the stack and set them as right and left children of the operator node
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        # If the term is a number, create a new tree node with the number
        node = TreeNode(int(term))
    # Push the new node onto the stack
    stack.push(node)

# Pop the root of the expression tree from the stack
root = stack.pop()

# Calculate the result of the expression tree
result = calc(root)

# Print the result
print(result)

# Visual representation of the expression tree:
#         *
#       /   \
#      +     -
#     / \   / \
#    4   5 5   3

# explaination 
# Sure! Let's break down the code step-by-step to understand what it does in detail.

# ### Overview

# The code evaluates a postfix (Reverse Polish Notation) expression using a binary expression tree. The expression given is `"4 5 + 5 3 - *"`, which is evaluated to produce the result `18`.

# ### Detailed Explanation

# #### 1. Stack Class

# The `Stack` class is a simple implementation of a stack data structure using a list.

# ```python
# class Stack:
#     def __init__(self):
#         # Initialize an empty list to store stack elements
#         self.elements = []
        
#     def push(self, item):
#         # Append an item to the stack
#         self.elements.append(item)
    
#     def pop(self):
#         # Remove and return the last item from the stack
#         return self.elements.pop()
# ```

# - **`__init__`**: Initializes an empty list to store stack elements.
# - **`push`**: Adds an item to the top of the stack.
# - **`pop`**: Removes and returns the item from the top of the stack.

# #### 2. TreeNode Class

# The `TreeNode` class represents a node in the binary expression tree.

# ```python
# class TreeNode:
#     def __init__(self, data=None):
#         # Initialize the tree node with data and set left and right children to None
#         self.data = data
#         self.right = None
#         self.left = None
# ```

# - **`__init__`**: Initializes the node with data and sets its left and right children to `None`.

# #### 3. calc Function

# The `calc` function recursively evaluates the expression tree.

# ```python
# def calc(node):
#     # Recursively calculate the value of the expression tree
#     if node.data == "+":
#         return calc(node.left) + calc(node.right)
#     elif node.data == "-":
#         return calc(node.left) - calc(node.right)
#     elif node.data == "*":
#         return calc(node.left) * calc(node.right)
#     elif node.data == "/":
#         return calc(node.left) / calc(node.right)
#     else:
#         return node.data
# ```

# - **`calc`**: Takes a `TreeNode` as input and recursively evaluates the expression tree based on the operator (`+`, `-`, `*`, `/`) or returns the numeric value if it's a leaf node.

# #### 4. Expression Evaluation

# The expression `"4 5 + 5 3 - *"` is split into individual terms and processed to build the expression tree.

# ```python
# expr = "4 5 + 5 3 - *".split()
# ```

# - **`split`**: Splits the expression string into a list of terms: `['4', '5', '+', '5', '3', '-', '*']`.

# #### 5. Building the Expression Tree

# The code iterates through each term in the expression to build the expression tree using a stack.

# ```python
# stack = Stack()

# for term in expr:
#     if term in "+-*/":
#         # If the term is an operator, create a new tree node with the operator
#         node = TreeNode(term)
#         # Pop two nodes from the stack and set them as right and left children of the operator node
#         node.right = stack.pop()
#         node.left = stack.pop()
#     else:
#         # If the term is a number, create a new tree node with the number
#         node = TreeNode(int(term))
#     # Push the new node onto the stack
#     stack.push(node)
# ```

# - **Stack Initialization**: An empty stack is initialized.
# - **Iteration**: The code iterates through each term in the expression.
#   - **Operator**: If the term is an operator (`+`, `-`, `*`, `/`), a new `TreeNode` is created with the operator. The top two nodes are popped from the stack and set as the right and left children of the operator node.
#   - **Operand**: If the term is a number, a new `TreeNode` is created with the number.
#   - **Push**: The new node is pushed onto the stack.

# #### 6. Evaluating the Expression Tree

# The root of the expression tree is popped from the stack, and the `calc` function is called to evaluate the expression.

# ```python
# root = stack.pop()
# result = calc(root)
# print(result)
# ```

# - **Pop Root**: The root of the expression tree is popped from the stack.
# - **Evaluate**: The `calc` function is called with the root node to evaluate the expression tree.
# - **Print Result**: The result of the evaluation is printed.

# ### Visual Representation of the Expression Tree

# ```
#          *
#        /   \
#       +     -
#      / \   / \
#     4   5 5   3
# ```

# ### Step-by-Step Evaluation

# 1. **Expression**: `"4 5 + 5 3 - *"`
# 2. **Split**: `['4', '5', '+', '5', '3', '-', '*']`
# 3. **Build Tree**:
#    - `4` -> Push `4`
#    - `5` -> Push `5`
#    - `+` -> Pop `5`, Pop `4`, Create `+` node, Push `+`
#    - `5` -> Push `5`
#    - `3` -> Push `3`
#    - `-` -> Pop `3`, Pop `5`, Create `-` node, Push `-`
#    - `*` -> Pop `-`, Pop `+`, Create `*` node, Push `*`
# 4. **Evaluate Tree**:
#    - `*` -> `+` * `-`
#    - `+` -> `4 + 5` = `9`
#    - `-` -> `5 - 3` = `2`
#    - `*` -> `9 * 2` = `18`

# ### Output

# - **Result**: `18`

# This detailed explanation should help you understand how the code works to evaluate the postfix expression using a binary expression tree. If you have any more questions or need further assistance, feel free to ask!