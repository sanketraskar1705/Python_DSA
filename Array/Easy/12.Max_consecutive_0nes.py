# Problem :- Max consecutive ones
#   Given a binary array nums, return the maximum number of consecutive 1's in the array.
from ast import List


class Solution:
    def maxConsecutiveOnes(self, arr):
        n = len(arr)
        max_count = 0
        count = 0
        for i in range(n):
            if arr[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0



        return max_count

s1= Solution()
arr = [1,0,1,1,0,1,1,1,1,0,1,1,1]
print(s1.maxConsecutiveOnes(arr))
