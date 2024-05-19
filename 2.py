def mark_brackets(input_lines):
    results = []

    for line in input_lines:
        stack = []
        output = list(line)  
        marker_output = [' ']*len(line) 
        
        for index, char in enumerate(line):
            if char == '(':
                stack.append(index)  # Push the index of '('
            elif char == ')':
                if stack:
                    stack.pop()  # Pop the last unmatched '('
                else:
                    # Mark a '?' below ')' if there is no matching '('
                    marker_output[index] = '?'
        
        # Place 'x' for each unmatched '(' in the stack
        while stack:
            left_index = stack.pop()
            if marker_output[left_index] == ' ':
                marker_output[left_index] = 'x'
            else:
                # If there is already a '?' from a previous mismatch, add 'x' beside it 
                marker_output[left_index] = 'x'
        
        # Join everything to form the final strings
        final_output = ''.join(output) + '\n' + ''.join(marker_output)
        results.append(final_output)
    
    return results

input_lines = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()"
]
output = mark_brackets(input_lines)
for line in output:
    print(line)


