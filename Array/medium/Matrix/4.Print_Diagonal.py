# Problem :- Print Diagonal of matrix

class Solution:
    def printDiagonal(self,nums):
        rows = len(nums)
        cols = len(nums[0])

        for i in range(rows):
            for j in range(cols):
                if j == i:
                    print(nums[i][j], end=" ")
                else:
                    print("*",end=" ")
            print()

s1 = Solution()
nums = [[-1,2,3],[4,-5,6],[-7,8,9]]
print(s1.printDiagonal(nums))
