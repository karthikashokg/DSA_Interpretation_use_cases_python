
size = 3
data = [0] * size  # Initialize the stack with a fixed size
top = -1  # Initialize the top pointer to -1, indicating the stack is empty

def push(x):
    global top
    if top >= size - 1:  # Check if the stack is full
        print("Stack Overflow")  # Print a message if the stack is full
    else:
        top = top + 1  # Increment the top pointer
        data[top] = x  # Add the new element to the top of the stack

def pop():
    global top
    if top == -1:  # Check if the stack is empty
        print("Stack Underflow")  # Print a message if the stack is empty
    else:
        top = top - 1  # Decrement the top pointer
        data[top + 1] = 0  # Reset the popped element to 0
        return data[top + 1]  # Return the popped element

def peek():
    global top
    if top == -1:  # Check if the stack is empty
        print("Stack is empty")  # Print a message if the stack is empty
    else:
        print(data[top])  # Print the top element of the stack

# Push elements onto the stack
push('egg')
push('ham')
push('spam')
push('new')  # This will print "Stack Overflow" because the stack can only hold 3 elements
push('new2')  # This will also print "Stack Overflow"

print(data[0:top + 1])  # Print the current elements in the stack
# Output: ['egg', 'ham', 'spam']

pop()  # Pop the top element ('spam')
pop()  # Pop the next top element ('ham')
pop()  # Pop the next top element ('egg')
pop()  # This will print "Stack Underflow" because the stack is now empty

print(data[0:top + 1])  # Print the current elements in the stack
# Output: []

peek()  # This will print "Stack is empty" because the stack is empty

print(data[0:top + 1])  # Print the current elements in the stack
# Output: []

################################################################################################

# ### Time and Space Complexities

# - **`push` function:**
#   - **Time Complexity:** O(1) for adding a new element to the stack.
#   - **Space Complexity:** O(1) for the additional element added to the stack.

# - **`pop` function:**
#   - **Time Complexity:** O(1) for removing the top element from the stack.
#   - **Space Complexity:** O(1) for the element removed from the stack.

# - **`peek` function:**
#   - **Time Complexity:** O(1) for accessing the top element's data.
#   - **Space Complexity:** O(1) as it does not modify the stack.

# ### Visual Representation

# Here's a visual representation of how the stack works:

# 1. **Initial State:**
#    ```
#    Stack: [0, 0, 0]
#    Top: -1
#    ```

# 2. **After Push 'egg':**
#    ```
#    Stack: ['egg', 0, 0]
#    Top: 0
#    ```

# 3. **After Push 'ham':**
#    ```
#    Stack: ['egg', 'ham', 0]
#    Top: 1
#    ```

# 4. **After Push 'spam':**
#    ```
#    Stack: ['egg', 'ham', 'spam']
#    Top: 2
#    ```

# 5. **Attempt to Push 'new' (Stack Overflow):**
#    ```
#    Stack: ['egg', 'ham', 'spam']
#    Top: 2
#    ```

# 6. **After Pop (removes 'spam'):**
#    ```
#    Stack: ['egg', 'ham', 0]
#    Top: 1
#    ```

# 7. **After Pop (removes 'ham'):**
#    ```
#    Stack: ['egg', 0, 0]
#    Top: 0
#    ```

# 8. **After Pop (removes 'egg'):**
#    ```
#    Stack: [0, 0, 0]
#    Top: -1
#    ```

# 9. **Attempt to Pop (Stack Underflow):**
#    ```
#    Stack: [0, 0, 0]
#    Top: -1
#    ```

# If you have any more questions or need further clarification, feel free to ask!