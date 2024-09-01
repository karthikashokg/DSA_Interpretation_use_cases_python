
def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]  # Stores unicode value of each character in text 
    ord_pattern = [ord(j) for j in pattern]  # Stores unicode value of each character in pattern
    len_text = len(text)  # Stores length of the text 
    len_pattern = len(pattern)  # Stores length of the pattern
    len_hash_array = len_text - len_pattern + 1  # Stores the length of new array that will contain the hash values of text
    hash_text = [0] * len_hash_array  # Initialize all the values in the array to 0.
    hash_pattern = sum(ord_pattern)  # Calculate the hash value for the pattern by summing unicode values

    for i in range(0, len_hash_array):  # Step size of the loop will be the size of the pattern
        if i == 0:  # Base condition
            hash_text[i] = sum(ord_text[:len_pattern])  # Initial value of hash function
        else:
            hash_text[i] = ((hash_text[i - 1] - ord_text[i - 1]) + ord_text[i + len_pattern - 1])  # Calculate next hash value using previous value

    return [hash_text, hash_pattern]  # Return the hash values

def Rabin_Karp_Matcher(text, pattern):
    text = str(text)  # Convert text into string format
    pattern = str(pattern)  # Convert pattern into string format
    hash_text, hash_pattern = generate_hash(text, pattern)  # Generate hash values using generate_hash function
    len_text = len(text)  # Length of text
    len_pattern = len(pattern)  # Length of pattern
    flag = False  # Checks if pattern is present at least once or not at all

    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern:  # If the hash value matches
            count = 0  # Count stores the total characters up to which both are similar
            for j in range(len_pattern):
                if pattern[j] == text[i + j]:  # Checking equality for each character
                    count += 1  # If value is equal, then update the count value
                else:
                    break
            if count == len_pattern:  # If count is equal to length of pattern, it means match has been found
                flag = True  # Update flag accordingly
                print('Pattern occurs at index', i)
    if not flag:  # If pattern doesn't match even once, then this if statement is executed
        print('Pattern is not at all present in the text')

# Function calls
Rabin_Karp_Matcher("101110000011010010101101", "10112")  # Pattern not found
Rabin_Karp_Matcher("101110000011010010101101", "1011")  # Pattern found
Rabin_Karp_Matcher("ABBACCADABBACCEDF", "ACCE")  # Pattern found
# ```

# ### Time and Space Complexities

# - **Time Complexity**:
#   - **Generate Hash (`generate_hash`)**: \(O(n)\), where \(n\) is the length of the text. This is because each character in the text is processed once to calculate the hash values.
#   - **Rabin-Karp Matcher (`Rabin_Karp_Matcher`)**: \(O(n \cdot m)\), where \(n\) is the length of the text and \(m\) is the length of the pattern. This is because, in the worst case, each character in the text is compared with each character in the pattern.

# - **Space Complexity**:
#   - **Generate Hash (`generate_hash`)**: \(O(n)\), for storing the hash values of the text.
#   - **Rabin-Karp Matcher (`Rabin_Karp_Matcher`)**: \(O(n)\), for storing the hash values of the text. The additional space used for the text and pattern is negligible.

# ### Interpretation

# The Rabin-Karp algorithm is a string matching algorithm that uses hashing to find any one of a set of pattern strings in a text. Here's a step-by-step interpretation:

# 1. **Generate Hash (`generate_hash`)**:
#    - Convert the text and pattern into their unicode values.
#    - Calculate the initial hash value for the pattern.
#    - Calculate the hash values for all possible substrings of the text that have the same length as the pattern.

# 2. **Rabin-Karp Matcher (`Rabin_Karp_Matcher`)**:
#    - Convert the text and pattern into string format.
#    - Generate the hash values for the text and pattern.
#    - Iterate through the hash values of the text.
#    - If a hash value matches the hash value of the pattern, compare the actual substrings to confirm the match.
#    - Print the starting index of the match if found.
#    - If no match is found, print a message.

# ### Example

# For the text `"101110000011010010101101"` and the pattern `"1011"`, the Rabin-Karp algorithm works as follows:

# 1. **Generate Hash**:
#    - Text: `"101110000011010010101101"`
#    - Pattern: `"1011"`
#    - Hash values for the text: `[49, 48, 49, 49, 48, 48, 48, 48, 49, 49, 48, 49, 48, 49, 48, 48, 49, 49, 48, 49, 48, 49, 48, 49]`
#    - Hash value for the pattern: `49`

# 2. **Matching**:
#    - The algorithm scans the text and compares the hash values.
#    - It finds matches at indices 0, 1, 2, and 3.

# This makes the Rabin-Karp algorithm efficient for multiple pattern matching, especially when the patterns are of the same length.

# Would you like any further details or another example?