# Problem :- Find missing number in list
# Optimal Solution

class Solution:
    def findElement(self, arr):
        n = len(arr)
        return (n*(n+1))//2 - sum(arr)

s1 = Solution()
arr = [1,0,3,2]
print(s1.findElement(arr))