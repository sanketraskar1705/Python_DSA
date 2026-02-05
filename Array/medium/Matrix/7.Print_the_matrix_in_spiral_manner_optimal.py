# Problem :- Print the matrix in spiral manner
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self,matrix):

        if not matrix or not matrix[0]:
            return [ ]

        result = []
        top , left = 0,0
        bottom, right = len(matrix)-1 ,len(matrix[0])-1

        while top <= bottom and left <= right:

            # left -> right  top row
            for i in range(left,right + 1):
                result.append(matrix[top][i])
            top += 1

            # top -> bottom (right column)
            for i in range(top,bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # right -> left (bottom row)
            if top <= bottom:
                for i in range(right,left - 1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # bottom -> top (left column)
            if left <= right:
                for i in range(bottom,top - 1,-1):
                    result.append(matrix[i][left])
                left += 1


        return result

s1 = Solution()
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

print(s1.spiralOrder(matrix))

"""
1. First, check if the matrix is empty.
   - If there are no elements, return an empty list.

2. Initialize four boundaries: top, bottom, left, right.
   - top    → first row index
   - bottom → last row index
   - left   → first column index
   - right  → last column index
   - These boundaries represent the current layer of the spiral.

3. Traverse from Left to Right across the top row.
   - Collect all elements from column left to right in row top.
   - Move the top boundary downward (top += 1).

4. Traverse from Top to Bottom along the right column.
   - Collect all elements from row top to bottom in column right.
   - Move the right boundary leftward (right -= 1).

5. Traverse from Right to Left across the bottom row (if valid).
   - Only perform if top <= bottom.
   - Collect elements from column right to left in row bottom.
   - Move the bottom boundary upward (bottom -= 1).

6. Traverse from Bottom to Top along the left column (if valid).
   - Only perform if left <= right.
   - Collect elements from row bottom to top in column left.
   - Move the left boundary rightward (left += 1).

7. Repeat steps 3–6.
   - Continue shrinking the boundaries inward
     until top > bottom OR left > right.

8. Return the collected spiral order list.

Time Complexity  : O(m × n)
Space Complexity : O(1) auxiliary (excluding output list)

"""