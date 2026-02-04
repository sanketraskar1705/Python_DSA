# Problem :- Rotate Matrix by 90 degrees
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation
"""
# Brute Solution
class Solution:
    def rotate(self,nums):
        n = len(nums)
        result = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                result[j][(n-1)-i]=nums[i][j]

        return result

s1 = Solution()
nums = [[1,2,3],[4,5,6],[7,8,9]]
print(s1.rotate(nums))