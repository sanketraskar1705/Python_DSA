# Problem :- Set Matrix Zeroes
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.You must do it in place.

# Brute Solution

class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        # Step 1: Mark rows and columns using infinity
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markInfinity(matrix, i, j)

        # Step 2: Convert infinity to zero
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0

    def markInfinity(self, matrix, row, col):
        r = len(matrix)
        c = len(matrix[0])

        # Mark column
        for i in range(r):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")

        # Mark row
        for j in range(c):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")


# -------- INPUT --------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix row-wise:")
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

# -------- PROCESS --------
obj = Solution()
obj.setZeroes(matrix)

# -------- OUTPUT --------
print("Matrix after setting zeroes:")
for row in matrix:
    print(row)

"""
1. We traverse the entire matrix.

2. Whenever we find a cell with value 0 at position (i, j),
   we do NOT immediately convert its entire row and column to 0.
   (Because that would affect other zero checks.)

3. Instead, we mark all non-zero elements in:
   - row i
   - column j
   with a temporary value (∞ / float("inf")).

4. This temporary value acts as a placeholder
   meaning "this cell must become zero later".

5. After the first full traversal is completed,
   we traverse the matrix again.

6. In the second traversal,
   every cell having value ∞ is converted to 0.

7. Original zeroes remain zero,
   and all required rows and columns are correctly set to zero.

8. The matrix is modified in-place.

"""