#Problem :- Count occurrences of a number in a sorted array with duplicates
# Optimal Solution
class Solution:
    def noOfoccurrence(self,nums,target):
        lb= self.lowerBound(nums,target)
        # target not present
        if lb == -1 or nums[lb] != target:
            return [-1, -1]
        ub = self.upperBound(nums, target)

        return ub-lb






    def lowerBound(self,nums,target):
        n = len(nums)
        lb = -1
        low , high = 0, n-1
        while low <= high:
            mid =(low+high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid -1
            else:
                low = mid + 1
        return lb

    def upperBound(self,nums,target):
        n  =len(nums)
        ub = n
        low,high=0,n-1
        while low <= high:
            mid = (low+high) //  2
            if nums[mid] > target:
                ub = mid
                high = mid -1
            else:
                low = mid + 1
        return ub

s1 = Solution()
nums = [1,1,2,2,2,2,3,4,6,6,7,8,9]
target = 1
print(s1.noOfoccurrence(nums,target))

"""
1. Goal:
   Count occurrences of target in a sorted array using Binary Search in O(log n).

2. Main Idea:
   Total occurrences = upperBound - lowerBound

------------------------------------------------------------

3. noOfoccurrence(nums, target):

   a) Call lowerBound(nums, target) → gives first index where element ≥ target (lb)

   b) If lb == -1 OR nums[lb] != target:
        → target not present
        → return 0

   c) Call upperBound(nums, target) → gives first index where element > target (ub)

   d) Total occurrences = ub - lb

   e) Return ub - lb

------------------------------------------------------------

4. lowerBound(nums, target):

   Purpose → Find first index where element ≥ target

   Steps:
   - Initialize lb = -1, low = 0, high = n-1
   - While low ≤ high:
       mid = (low + high) // 2
       If nums[mid] ≥ target:
           lb = mid        (possible first occurrence)
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
           ub = mid        (first element greater than target)
           move left → high = mid - 1
       Else:
           move right → low = mid + 1
   - Return ub

------------------------------------------------------------

6. Why ub - lb gives total occurrences?

   lowerBound → first position of target
   upperBound → first position greater than target
   Difference (ub - lb) = total count of target

------------------------------------------------------------

7. Time Complexity  : O(log n)
8. Space Complexity : O(1)
"""