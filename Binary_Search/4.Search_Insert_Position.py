# Problem :- Search Insert Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
# Optimal Solution
class Solution:
    def serchInsert(self,nums,target):
        n = len(nums)
        low = 0
        high = n-1
        lb = n
        while low <= high:
            mid = (low+ high)//2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

s1 = Solution()
nums = [1,3,5,7]
target = 10
print(s1.serchInsert(nums,target))

"""
Logic :-

1. We need to find the index where target exists OR where it should be inserted.
   This is exactly the LOWER BOUND:
   → smallest index i such that nums[i] >= target

2. Initialize:
   - low = 0
   - high = n-1
   - lb = n  (default answer if target is greater than all elements)

3. Apply Binary Search:

4. While low <= high:
      - mid = (low + high) // 2

      Case 1: nums[mid] >= target
              → This can be the answer.
              → Store lb = mid
              → But we want the FIRST such index, so move LEFT.
              → high = mid - 1

      Case 2: nums[mid] < target
              → Target must be on RIGHT side.
              → low = mid + 1

5. When loop ends, lb is:
      - index of target (if found)
      - OR index where it should be inserted

6. Return lb

Time Complexity  : O(log n)  
Space Complexity : O(1)
"""
