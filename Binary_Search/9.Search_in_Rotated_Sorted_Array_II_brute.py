# Problem :- Search in Rotated Sorted Array II
"""
Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.
"""

# Brute Solution
class Solution:
    def search(self,nums,target):
        n=len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return True

        return False

s1 = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(s1.search(nums, target))
"""
1. Goal:
   Check whether target exists in the array.
   If present → return True
   If not present → return False

2. Initialize:
   n = length of array

3. Traverse the array from index 0 to n-1.

4. For each index i:
   - If nums[i] == target:
       → target found
       → return True immediately

5. If loop completes and target is not found:
   → return False

------------------------------------------------------------

Time Complexity  : O(n)
Space Complexity : O(1)
"""