# Problem :- Rotate Matrix by 90 degrees
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation
"""
# Optimal Solution

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0,n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

        return matrix

s1 = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s1.rotate(matrix))

"""
1. First, we transpose the matrix.
   - Transpose means converting rows into columns.
   - For every cell (i, j), swap it with (j, i).
   - We only swap elements where j > i to avoid double swapping.

2. After transposing, each row of the matrix is reversed.
   - Reversing each row gives the final 90° clockwise rotation.

3. The rotation is done in-place.
   - No extra matrix is used.

Time Complexity  : O(n²)
Space Complexity : O(1)


"""