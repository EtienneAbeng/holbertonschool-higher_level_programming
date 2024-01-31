#!/usr/bin/python3

def print_matrix_integer(matrix=None):
    # Check if the matrix is empty or does not exist
    if matrix is None or not matrix or not matrix[0]:
        print("")
        return

    # Go through each row in the matrix
    for row in matrix:
        # Go through each number in the row
        for idx, number in enumerate(row):
            # Print the number with a space after it, except for the last number
            print("{:d}".format(number), end=" ")
            
            # Start a new line if it's the last number in the row
            if idx == len(row) - 1:
                print()

# Example of how to use the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function with the example matrix
print_matrix_integer(matrix)

