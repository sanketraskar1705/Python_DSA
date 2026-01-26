# Problem :- Find the missing number in list
# Brute Solution

class Solution:
    def findElement(self,arr):
        n = len(arr)
        for i in range(n+1):
            if i not in arr:
                return i

s1 = Solution()
arr = [0,2,1,4]
print(s1.findElement(arr))
