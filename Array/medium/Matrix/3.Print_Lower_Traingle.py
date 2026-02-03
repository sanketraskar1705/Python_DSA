# Problem :- Print lower tringle

class Solution:
    def printLower( self, nums ):
        rows = len(nums)
        cols = len(nums[0])

        for i in range(rows):
            for j in range(cols):
                if j <= i :
                    print(nums[i][j], end=" ")
                else:
                    print("*", end=" ")
            print()

        

s1 = Solution()
nums =[[23,-3,67],[12,8,-31],[-78,82,45]]
print(s1.printLower(nums))


