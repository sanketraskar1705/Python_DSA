# Problem:- Find First and Last Position of Element in Sorted Array
"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
# Optimal solution
class Solution:
    def searchRange(self, nums, target):
        lb = self.lowerBound(nums, target)

        # target not present
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = self.upperBound(nums, target)
        return [lb, ub - 1]

    def lowerBound(self,nums,target):
        n= len(nums)
        lb = -1
        low,high=0,n-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upperBound(self,nums,target):
        n = len(nums)
        ub = n
        low, high = 0, n - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

s1 = Solution()
nums = [1,1,1,2,3,4,4,5,5,6,7,8,8,8,8,9]
target = 8
print(s1.searchRange(nums,target))

"""
1. Goal:
   Find the first and last occurrence of target in a sorted array using Binary Search in O(log n).

2. Main Idea:
   - First occurrence = Lower Bound (first index where element ≥ target)
   - Last occurrence  = Upper Bound - 1 (last index where element = target)

------------------------------------------------------------

3. searchRange(nums, target):

   a) Call lowerBound(nums, target) → gives first possible position of target (lb)

   b) If lb == -1 OR nums[lb] != target:
        → target not present in array
        → return [-1, -1]

   c) Call upperBound(nums, target) → gives first index where element > target (ub)

   d) Last occurrence = ub - 1

   e) Return [lb, ub - 1]

------------------------------------------------------------

4. lowerBound(nums, target):

   Purpose → Find first index where element ≥ target

   Steps:
   - Initialize lb = -1, low = 0, high = n-1
   - While low ≤ high:
       mid = (low + high) // 2
       If nums[mid] ≥ target:
           lb = mid        (possible answer)
           move left → high = mid - 1
       Else:
           move right → low = mid + 1
   - Return lb

------------------------------------------------------------

5. upperBound(nums, target):

   Purpose → Find first index where element > target

   Steps:
   - Initialize ub = n, low = 0, high = n-1
   - While low ≤ high:
       mid = (low + high) // 2
       If nums[mid] > target:
           ub = mid        (possible answer)
           move left → high = mid - 1
       Else:
           move right → low = mid + 1
   - Return ub

------------------------------------------------------------

6. Why ub - 1 gives last occurrence?

   upperBound returns first index where element > target,
   so previous index (ub - 1) is the last index where element == target.

------------------------------------------------------------

7. Time Complexity  : O(log n)
8. Space Complexity : O(1)
"""