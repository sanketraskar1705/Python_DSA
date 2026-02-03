# Problem :- Print Upper Triangle

class Solution:
    def matrix(self, nums):
        rows = len(nums)
        cols = len(nums[0])

        for i in range(rows):
            for j in range(cols):
                if j >= i:
                    print(nums[i][j], end=" ")
                else:
                    print("*", end=" ")

            print()


s1 = Solution()
nums = [[1,-82,3],[34,51,6],[17,-8,9]]
print(s1.matrix(nums))