# Problem :- Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# Brute Solution

class Solution:
    def search(self, nums, target):
        n = len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return i
        return -1

s1 = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s1.search(nums,target))

"""
1. Goal:
   Find the index of target in the array.
   If target is not present → return -1.

2. Initialize:
   n = length of array

3. Traverse the array from index 0 to n-1.

4. For each index i:
   - If nums[i] == target:
       → target found
       → return index i immediately

5. If loop finishes and target is not found:
   → return -1

------------------------------------------------------------

Time Complexity  : O(n)
Space Complexity : O(1)
"""