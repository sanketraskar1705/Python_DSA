# Problem :- Maximum subarray
# # Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_val = float("-inf")
        total = 0
        for i in range(n):
            total += nums[i]
            max_val = max(max_val, total)
            if total < 0:
                total = 0
        return max_val

s1 = Solution()
nums = [-2,1,-3,4]
print(s1.maxSubArray(nums))

"""
Logic (Kadane’s Algorithm):

- We iterate through the array and keep a running sum (total).
- At each index:
    1. Add the current element to total.
    2. Update max_val with the maximum of max_val and total.
    3. If total becomes negative, reset it to 0.
       (Because a negative sum will reduce future subarray sums)

- max_val always stores the maximum subarray sum found so far.

Edge Case:
- max_val starts with -infinity to handle arrays with all negative numbers.

Time Complexity: O(n)
Space Complexity: O(1)
"""
