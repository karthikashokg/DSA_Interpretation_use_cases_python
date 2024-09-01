
def pfun(pattern):          # Function to generate prefix function for the given pattern
    n = len(pattern)        # Length of the pattern
    prefix_fun = [0] * n    # Initialize all elements of the list to 0
    k = 0                   # Length of the previous longest prefix suffix

    for q in range(2, n):
        while k > 0 and pattern[k + 1] != pattern[q]:
            k = prefix_fun[k]  # Fall back in the pattern
        if pattern[k + 1] == pattern[q]:  # If the kth element of the pattern is equal to the qth element
            k += 1  # Update k accordingly
        prefix_fun[q] = k  # Set the prefix function value for position q

    return prefix_fun  # Return the prefix function

def KMP_Matcher(text, pattern):  # KMP matcher function
    m = len(text)  # Length of the text
    n = len(pattern)  # Length of the pattern
    flag = False  # Flag to indicate if a match is found
    text = '-' + text  # Append dummy character to make it 1-based indexing
    pattern = '-' + pattern  # Append dummy character to the pattern also
    prefix_fun = pfun(pattern)  # Generate prefix function for the pattern
    q = 0  # Number of characters matched

    for i in range(1, m + 1):
        while q > 0 and pattern[q + 1] != text[i]:  # While pattern and text are not equal, decrement the value of q if it is > 0
            q = prefix_fun[q]  # Fall back in the pattern
        if pattern[q + 1] == text[i]:  # If pattern and text are equal, update value of q
            q += 1
        if q == n:  # If q is equal to the length of the pattern, it means that the pattern has been found
            print("Pattern occurs with shift", i - n)  # Print the index where the first match occurs
            flag = True
            q = prefix_fun[q]  # Prepare for the next potential match

    if not flag:
        print('\nNo match found')  # If no match is found, print a message

# Function call with text and pattern
KMP_Matcher('aabaacaadaabaaba', 'aabaa')
# ```

# ### Time and Space Complexities

# - **Time Complexity**:
#   - **Prefix Function (`pfun`)**: \(O(n)\), where \(n\) is the length of the pattern. This is because each character in the pattern is processed once.
#   - **KMP Matcher (`KMP_Matcher`)**: \(O(m + n)\), where \(m\) is the length of the text and \(n\) is the length of the pattern. This is because the text is scanned once and the pattern is processed using the prefix function.

# - **Space Complexity**:
#   - **Prefix Function (`pfun`)**: \(O(n)\), for storing the prefix function array.
#   - **KMP Matcher (`KMP_Matcher`)**: \(O(n)\), for storing the prefix function array. The additional space used for the text and pattern is negligible.

# ### Interpretation

# The Knuth-Morris-Pratt (KMP) algorithm is an efficient string matching algorithm that uses a preprocessing step to create a prefix function for the pattern. This prefix function helps in avoiding unnecessary comparisons by skipping over parts of the text that have already been matched.

# 1. **Prefix Function (`pfun`)**:
#    - The prefix function is an array that stores the length of the longest proper prefix which is also a suffix for each position in the pattern.
#    - This helps in determining how much to shift the pattern when a mismatch occurs.

# 2. **KMP Matcher (`KMP_Matcher`)**:
#    - The text and pattern are modified to use 1-based indexing by adding a dummy character at the beginning.
#    - The prefix function for the pattern is generated.
#    - The algorithm scans the text and compares it with the pattern using the prefix function to skip over already matched characters.
#    - When a match is found, the starting index of the match is printed.
#    - If no match is found, a message is printed.

# ### Example

# For the text `'aabaacaadaabaaba'` and the pattern `'aabaa'`, the KMP algorithm works as follows:

# 1. **Prefix Function**:
#    - Pattern: `aabaa`
#    - Prefix Function: `[0, 0, 1, 0, 1]`

# 2. **Matching**:
#    - The algorithm scans the text and uses the prefix function to skip over already matched characters.
#    - It finds matches at indices 0 and 9.

# This makes the KMP algorithm more efficient than the brute force approach, especially for large texts and patterns.

# Would you like any further details or another example?