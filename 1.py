from collections import defaultdict
import bisect

def minimum_sequences(source, target):
    char_positions = defaultdict(list)
    for index, char in enumerate(source):
        char_positions[char].append(index)
    
    if any(char not in char_positions for char in target):
        return -1

    num_subsequences = 0
    i = 0  
    while i < len(target):
        num_subsequences += 1
        current_source_index = -1  

        while i < len(target):
            char = target[i]
            if char not in char_positions:
                return -1  # not possible to form target
            
            # List of positions in source where current target char appears
            positions = char_positions[char]
            # Find the smallest position in positions that is greater than current_source_index
            pos_index = bisect.bisect_right(positions, current_source_index)
            if pos_index == len(positions):
                break  # need to start a new subsequence
            
            # Update current_source_index to the found position
            current_source_index = positions[pos_index]
            i += 1  # move to the next character in target

    return num_subsequences

print(minimum_sequences("abc", "abcbc"))  
print(minimum_sequences("abc", "acdbc")) 
print(minimum_sequences("xyz", "xzyxz")) 
