# Problem :- Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.You must do it in place.

# optimal Solution

class Solution:
    def solve(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        rowtrack = [0] * r
        coltrack = [0] * c
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(r):
            for j in range(c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0

        return matrix

s1 = Solution()
matrix = [[1,0,1],[1,1,0],[1,1,1]]
print(s1.solve(matrix))

"""
LOGIC – SET MATRIX ZEROES (OPTIMAL APPROACH)

1. Find the number of rows (r) and columns (c) in the matrix.

2. Create two extra arrays:
   - rowtrack of size r to track which rows contain at least one zero.
   - coltrack of size c to track which columns contain at least one zero.

3. Traverse the entire matrix:
   - If matrix[i][j] is equal to 0,
     mark rowtrack[i] = -1 and coltrack[j] = -1.
   - This indicates that the entire row i and column j must be set to zero.

4. Traverse the matrix again:
   - For each cell matrix[i][j],
     if rowtrack[i] == -1 OR coltrack[j] == -1,
     set matrix[i][j] = 0.

5. The matrix is modified in place and returned as the final answer.

TIME COMPLEXITY:
- O(m × n), because the matrix is traversed twice.

SPACE COMPLEXITY:
- O(m + n), for storing row and column markers.
"""


