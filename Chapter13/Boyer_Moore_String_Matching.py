
text = "acbaacacababacacac"
pattern = "acacac"

matched_indexes = []  # List to store the starting indexes of matched patterns

i = 0  # Initialize the starting index for the text
flag = True  # Flag to indicate if a match is found

while i <= len(text) - len(pattern):  # Loop until the end of the text minus the length of the pattern
    for j in range(len(pattern) - 1, -1, -1):  # Reverse searching in the pattern
        if pattern[j] != text[i + j]:  # If characters do not match
            flag = False  # Set flag to False indicating a mismatch
            if j == len(pattern) - 1:  # If the mismatch is at the last character of the pattern
                if text[i + j] in pattern[0:j]:  # Check if the bad character is in the pattern
                    i = i + j - pattern[0:j].rfind(text[i + j])  # Jump to the position of the bad character in the pattern
                else:
                    i = i + j + 1  # If the bad character is not in the pattern, jump to the next character
            else:
                k = 1
                while text[i + j + k:i + len(pattern)] not in pattern[0:len(pattern) - 1]:  # Find sub part of a good-suffix
                    k = k + 1
                if len(text[i + j + k:i + len(pattern)]) != 1:  # Good-suffix should not be of one character
                    gsshift = i + j + k - pattern[0:len(pattern) - 1].rfind(text[i + j + k:i + len(pattern)])  # Jump to the position where good-suffix matches
                else:
                    gsshift = 0  # Prefer bad character heuristic if good-suffix heuristic is not applicable
                if text[i + j] in pattern[0:j]:
                    bcshift = i + j - pattern[0:j].rfind(text[i + j])  # Jump to the position of the bad character in the pattern
                else:
                    bcshift = i + j + 1
                i = max((bcshift, gsshift))  # Choose the maximum shift
            break
    if flag:  # If pattern is found
        matched_indexes.append(i)  # Append the starting index to the list
        i = i + 1  # Move to the next character
    else:  # Reset flag to True for the next iteration
        flag = True

print("Pattern found at", matched_indexes)  # Print the matched indexes
# ```

# ### Time and Space Complexities

# - **Time Complexity**: The worst-case time complexity is \(O(n \cdot m)\), where \(n\) is the length of the text and \(m\) is the length of the pattern. This is because, in the worst case, each character in the text is compared with each character in the pattern.
# - **Space Complexity**: The space complexity is \(O(1)\) for the algorithm itself, as it uses a constant amount of extra space. However, the space complexity for storing the matched indexes is \(O(k)\), where \(k\) is the number of matches found.

# ### Interpretation

# The algorithm is a variation of the Boyer-Moore string search algorithm, which uses two heuristics: the bad character heuristic and the good suffix heuristic. Here's a step-by-step interpretation:

# 1. **Initialization**:
#    - The text and pattern are given.
#    - An empty list `matched_indexes` is created to store the starting indexes of matches.
#    - The index `i` is initialized to 0, and a flag is set to True.

# 2. **Reverse Searching**:
#    - The algorithm starts comparing the pattern with the text from the end of the pattern.
#    - If a mismatch is found, the flag is set to False.

# 3. **Bad Character Heuristic**:
#    - If the mismatch occurs at the last character of the pattern, the algorithm checks if the bad character exists in the pattern.
#    - If it exists, the pattern is shifted to align the bad character in the text with the same character in the pattern.
#    - If it does not exist, the pattern is shifted to the next character in the text.

# 4. **Good Suffix Heuristic**:
#    - If the mismatch occurs before the last character, the algorithm looks for a good suffix in the pattern.
#    - It shifts the pattern to align the good suffix in the text with the same suffix in the pattern.
#    - If the good suffix heuristic is not applicable, the bad character heuristic is used.

# 5. **Match Found**:
#    - If the flag remains True after comparing all characters, a match is found, and the starting index is added to the list.
#    - The index `i` is incremented to continue searching for the next match.

# 6. **Output**:
#    - The matched indexes are printed.

# This algorithm efficiently finds all occurrences of the pattern in the text using the Boyer-Moore heuristics, making it faster than a naive string matching algorithm in many cases.

# Would you like any further details or another example?