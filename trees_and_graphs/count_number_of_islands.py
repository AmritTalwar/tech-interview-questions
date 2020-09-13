# SOURCE: https://leetcode.com/problems/number-of-islands/submissions/

"""
TIME SPACE ANALYSIS: basically the same as riverSizes.py
"""


def count_number_of_islands(matrix):
    number_of_islands = 0

    # Create matrix of same dimensions to keep track of visited nodes so we dont double count nodes
    visited = [[False for value in row] for row in matrix]

    # For each node in the matrix, perform a DFS on any pieces of land, marking nodes as visited along the way to prevent doublecounting
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            # Only DFS on unvisited pieces of land and iterate the number of islands each DFS call (this will count all unique islands)
            if visited[row][col]:
                continue
            if matrix[row][col] == "0":
                continue

            # DFS this land to 'discover' it all so all nodes can be marked as visited to prevent us from double counting this bit of land
            DFS(row, col, matrix, visited)
            number_of_islands += 1

    return number_of_islands


def DFS(row, col, matrix, visited):
    # Once we have reached a visited node or a piece of river, we know to end the search
    if visited[row][col]:
        return

    # Mark the node as explored/ visited
    visited[row][col] = True

    if matrix[row][col] == "0":
        return

    # DFS UP, DOWN, LEFT, RIGHT
    if row >= 1:
        DFS(row - 1, col, matrix, visited)
    if row + 1 < len(matrix):
        DFS(row + 1, col, matrix, visited)
    if col >= 1:
        DFS(row, col - 1, matrix, visited)
    if col + 1 < len(matrix[0]):
        DFS(row, col + 1, matrix, visited)
