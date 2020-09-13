// SOURCE: https://leetcode.com/problems/flood-fill/

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColour
 * @return {number[][]}
 *
 * TIME COMPLEXITY: O(N) N = number of coords in grid
 * We visit each coord in the grid and perform an O(1) operation
 *
 * SPACE COMPLEXITY: O(N)
 * Worst case we colour in all the grid, giving us a call stack of size N when performing the depth first search
 */

const floodFill = (image, sr, sc, newColour) => {
  const rowsLength = image.length;
  const columnsLength = image[0].length;

  const startingColour = image[sr][sc];

  const startPointAlreadyColoured = startingColour === newColour;
  if (startPointAlreadyColoured) {
    return image;
  }

  const depthFirstSearch = (row, col) => {
    const colour = image[row][col];
    if (colour === startingColour) {
      image[row][col] = newColour;

      // DFS UP
      if (row >= 1) {
        depthFirstSearch(row - 1, col);
      }

      // DFS DOWN
      if (row + 1 < rowsLength) {
        depthFirstSearch(row + 1, col);
      }

      // DFS LEFT
      if (col >= 1) {
        depthFirstSearch(row, col - 1);
      }

      // DFS RIGHT
      if (col + 1 < columnsLength) {
        depthFirstSearch(row, col + 1);
      }
    }
  };

  depthFirstSearch(sr, sc);
  return image;
};
