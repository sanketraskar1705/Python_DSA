# Problem :- Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Brute Solution
class Solution:
    def twoSum(self,arr,target):
        n = len(arr)
        for i in range(0,n-1):
            for j in range(i+1,n):
                if arr[i]+arr[j] == target:
                    return [i,j]


s1 = Solution()
arr = [2,7,11,15]
target = 26
print(s1.twoSum(arr,target))
