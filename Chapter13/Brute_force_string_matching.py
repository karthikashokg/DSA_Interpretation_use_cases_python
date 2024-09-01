
def brute_force(text, pattern):
    l1 = len(text)      # The length of the text string
    l2 = len(pattern)   # The length of the pattern 
    i = 0
    j = 0               # Looping variables are set to 0
    flag = False        # If the pattern doesn't appear at all, then set this to False and execute the last if statement

    while i < l1:       # Iterating from the 0th index of text
        j = 0
        count = 0       # Count stores the length up to which the pattern and the text have matched

        while j < l2:
            if i + j < l1 and text[i + j] == pattern[j]:  
                # Statement to check if a match has occurred or not
                count += 1     # Count is incremented if a character is matched 
            j += 1

        if count == l2:   # It shows a matching of pattern in the text 
            print("\nPattern occurs at index", i) 
            # Print the starting index of the successful match
            flag = True 
            # Flag is True as we wish to continue looking for more matching of pattern in the text. 

        i += 1

    if not flag: 
        # If the pattern doesn't occur at all, means no match of pattern in the text string
        print('\nPattern is not at all present in the array')

# Function call
brute_force('acbcabccababcaacbcac', 'acbcac')
# ```

# ### Time and Space Complexities

# - **Time Complexity**: The time complexity of this brute force algorithm is \(O(n \cdot m)\), where \(n\) is the length of the text and \(m\) is the length of the pattern. This is because, in the worst case, each character in the text is compared with each character in the pattern.
# - **Space Complexity**: The space complexity is \(O(1)\) as the algorithm uses a constant amount of extra space regardless of the input size.

# ### Interpretation

# The brute force algorithm for pattern matching works by checking every possible position in the text where the pattern could start and comparing the characters one by one. Here's a step-by-step interpretation:

# 1. **Initialization**:
#    - The lengths of the text and pattern are calculated.
#    - Looping variables `i` and `j` are initialized to 0.
#    - A flag is set to False to indicate if the pattern is found.

# 2. **Outer Loop**:
#    - The outer loop iterates through each character in the text from the start to the end minus the length of the pattern.

# 3. **Inner Loop**:
#    - The inner loop iterates through each character in the pattern.
#    - For each character in the pattern, it checks if it matches the corresponding character in the text.
#    - If a match is found, the count is incremented.

# 4. **Pattern Match Check**:
#    - After the inner loop, if the count equals the length of the pattern, it means the pattern is found at the current index `i`.
#    - The starting index of the match is printed, and the flag is set to True.

# 5. **Continue Searching**:
#    - The outer loop continues to search for more occurrences of the pattern in the text.

# 6. **No Match Found**:
#    - If the flag remains False after the outer loop, it means the pattern is not found in the text, and a message is printed.

# This algorithm is straightforward but can be inefficient for large texts and patterns due to its \(O(n \cdot m)\) time complexity. However, it is easy to understand and implement.

# Would you like any further details or another example?