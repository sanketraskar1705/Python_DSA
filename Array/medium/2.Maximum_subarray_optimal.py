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