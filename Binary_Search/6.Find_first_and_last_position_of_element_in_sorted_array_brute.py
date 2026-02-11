# Problem:- Find First and Last Position of Element in Sorted Array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
# Brute solution
class Solution:
    def positionOfelement(self,nums,target):
        n = len(nums)
        first = -1
        last = -1

        for i in range(0,n):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first,last]

s1 = Solution()
nums = [1,1,1,2,3,4,4,5,5,6,7,8,8,8,8,9]
target = 8
print(s1.positionOfelement(nums,target))

"""
1. Initialize:
   first = -1 (to store first occurrence index)
   last  = -1 (to store last occurrence index)

2. Traverse the array from index 0 to n-1:

3. For each element:
   - If nums[i] == target:
       a) If first == -1 → this is the first time target is found
          → set first = i
       b) Always update last = i
          → this keeps track of the most recent (last) occurrence

4. After completing the loop:
   - If target never appeared → first and last remain -1
   - Otherwise → first = first index of target, last = last index of target

5. Return [first, last]

Time Complexity  : O(n)
Space Complexity : O(1)
"""