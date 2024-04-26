#!/usr/bin/python3
"""Pascal's triangle"""

def pascal_triangle(n):
    """a function that returns a list of lists of integers
    representing the pascal's triangle"""
    if n <= 0:
        return []  # Return an empty list if n <= 0

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)  # Initialize each row with 1s
        for j in range(1, i):
            # Calculate each element in the middle of the row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)  # Append the row to the triangle

    return triangle
