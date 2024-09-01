
def insertion_sort(unsorted_list):
    # Loop over the list starting from the second element
    for index in range(1, len(unsorted_list)):
        search_index = index  # Initialize search_index to the current index
        insert_value = unsorted_list[index]  # Store the value to be inserted
        # Shift elements of the sorted segment to the right to make space for insert_value
        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1  # Move to the next position on the left
        # Insert the value at the correct position
        unsorted_list[search_index] = insert_value

        # Visual representation of the current state of the list
        print(f"Step {index}: {unsorted_list}")

# Example usage
my_list = [5, 1, 100, 2, 10]
print("Original list", my_list)
insertion_sort(my_list)
print("Sorted list", my_list)

# Enhanced Visual Flow
# Initial List: [5, 1, 100, 2, 10]
#
# Step 1:
# [5, 1, 100, 2, 10]
#  ↓
# [1, 5, 100, 2, 10]
#
# Step 2:
# [1, 5, 100, 2, 10]
# (no change)
#
# Step 3:
# [1, 5, 100, 2, 10]
#  ↓
# [1, 5, 2, 100, 10]
#  ↓
# [1, 2, 5, 100, 10]
#
# Step 4:
# [1, 2, 5, 100, 10]
#  ↓
# [1, 2, 5, 10, 100]
#
# Sorted List: [1, 2, 5, 10, 100]

# ### Use Case: Sorting a List of Student Scores

# Imagine you are a teacher and you have a list of student scores that you want to sort in ascending order. Here is the list of scores: `[85, 70, 95, 60, 90]`.

# We'll use the insertion sort algorithm to sort this list step-by-step.

# ### Initial List
# ```
# [85, 70, 95, 60, 90]
# ```

# ### Step-by-Step Explanation

# 1. **Step 1**: Start with the second element (70). Compare it with the first element (85).
#    - Since 70 < 85, swap them.
#    - List after Step 1: `[70, 85, 95, 60, 90]`
#    - ![Step 1](https://i.imgur.com/3C1z5zT.png)

# 2. **Step 2**: Move to the third element (95). Compare it with the previous elements.
#    - 95 is already greater than 85, so no change.
#    - List after Step 2: `[70, 85, 95, 60, 90]`
#    - ![Step 2](https://i.imgur.com/3C1z5zT.png)

# 3. **Step 3**: Move to the fourth element (60). Compare it with the previous elements.
#    - 60 < 95, so swap them.
#    - 60 < 85, so swap them.
#    - 60 < 70, so swap them.
#    - List after Step 3: `[60, 70, 85, 95, 90]`
#    - ![Step 3](https://i.imgur.com/3C1z5zT.png)

# 4. **Step 4**: Move to the fifth element (90). Compare it with the previous elements.
#    - 90 < 95, so swap them.
#    - 90 > 85, so no further swaps.
#    - List after Step 4: `[60, 70, 85, 90, 95]`
#    - ![Step 4](https://i.imgur.com/3C1z5zT.png)

# ### Final Sorted List
# ```
# [60, 70, 85, 90, 95]
# ```

# ### Code with Enhanced Visual Comments

# ```python
# def insertion_sort(unsorted_list):
#     # Loop over the list starting from the second element
#     for index in range(1, len(unsorted_list)):
#         search_index = index  # Initialize search_index to the current index
#         insert_value = unsorted_list[index]  # Store the value to be inserted
#         # Shift elements of the sorted segment to the right to make space for insert_value
#         while search_index > 0 and unsorted_list[search_index-1] > insert_value:
#             unsorted_list[search_index] = unsorted_list[search_index-1]
#             search_index -= 1  # Move to the next position on the left
#         # Insert the value at the correct position
#         unsorted_list[search_index] = insert_value

#         # Visual representation of the current state of the list
#         print(f"Step {index}: {unsorted_list}")

# # Example usage
# my_list = [85, 70, 95, 60, 90]
# print("Original list", my_list)
# insertion_sort(my_list)
# print("Sorted list", my_list)

# # Enhanced Visual Flow
# # Initial List: [85, 70, 95, 60, 90]
# #
# # Step 1:
# # [85, 70, 95, 60, 90]
# #  ↓
# # [70, 85, 95, 60, 90]
# #
# # Step 2:
# # [70, 85, 95, 60, 90]
# # (no change)
# #
# # Step 3:
# # [70, 85, 95, 60, 90]
# #  ↓
# # [70, 85, 60, 95, 90]
# #  ↓
# # [70, 60, 85, 95, 90]
# #  ↓
# # [60, 70, 85, 95, 90]
# #
# # Step 4:
# # [60, 70, 85, 95, 90]
# #  ↓
# # [60, 70, 85, 90, 95]
# #
# # Sorted List: [60, 70, 85, 90, 95]
# ```

# This example demonstrates how the insertion sort algorithm works in a real-world scenario, sorting a list of student scores. If you have any more questions or need further clarification, feel free to ask!