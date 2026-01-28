# Problem :- Maximum subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.



class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_val = float('-inf')
        for i in range(0,n):
            total = 0
            for j in range(i,n):
                total = total + nums[j]
                max_val = max(max_val,total)
        return max_val

s1 = Solution()
nums = [-2,1,-3,4]
print(s1.maxSubArray(nums))