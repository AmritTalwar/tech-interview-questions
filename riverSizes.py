"""
TIME COMPLEXITY: O(N) N = number of points in the matrix.

Because we are using a duplicate matrix to keep track of visited coords, we only visit each coord once
and perform O(1) operations on it.

SPACE COMPLEXITY: O(N)

This is because we are storing a duplicate matrix with N coords in it. It is also the size of the recurssion callstack
during DFS in the worst case scenario when all the matrix is one big river (DFS stack here will grow as big as the number of points).
"""


def riverSizes(matrix):
    # store the river sizes to be returned by the fn
    sizes = []

    # create a matrix of duplicate dimensions to keep track of visited coords to prevent looping
    visited = [[False for value in row] for row in matrix]

    counter = 0
    # for every coord in matrix
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            counter += 1
            print(counter)
            # if we have already visited the coord, then we skip DFS'ing through it
            if visited[row][col]:
                continue
            # DFS through the current point with a starting river size of 0 (this point could be river or land)
            size = DFS(row, col, matrix, visited, 0)
            if size > 0:
                sizes.append(size)
    return sizes


def DFS(row, col, matrix, visited, currentRiverSize):
    # if we encounter a previously visited coord (i.e. the river loops back in on itself) then return the current river size
    if visited[row][col]:
        return currentRiverSize

    # mark coord as visited
    visited[row][col] = True

    # if the coord === 0, we have hit land so the river has ended at this current point in the DFS, so return the current value
    if matrix[row][col] == 0:
        return currentRiverSize

    currentRiverSize += 1

    # DFS UP
    if row >= 1:
        currentRiverSize = DFS(row - 1, col, matrix, visited, currentRiverSize)

    # DFS DOWN
    if row + 1 < len(matrix):
        currentRiverSize = DFS(row + 1, col, matrix, visited, currentRiverSize)

    # DFS LEFT
    if col >= 1:
        currentRiverSize = DFS(row, col - 1, matrix, visited, currentRiverSize)

    # DFS RIGHT
    if col + 1 < len(matrix[0]):
        currentRiverSize = DFS(row, col + 1, matrix, visited, currentRiverSize)

    return currentRiverSize


test1 = [[1, 1, 1], [1, 0, 1]]
print(riverSizes(test1))