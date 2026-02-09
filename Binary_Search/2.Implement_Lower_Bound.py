# Problem:- Floor in a Sorted Array
"""
Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x.
This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of floor of x, return the index of the last occurrence."""

# Floor in a Sorted Array
class Solution:
    def floorIndex(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = -1   # store index of floor

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] <= target:
                ans = mid          # possible floor
                low = mid + 1      # try to find larger <= target
            else:
                high = mid - 1

        return ans


s1 = Solution()
nums = [1, 2, 8, 10, 10, 12, 19]
target = 5
print(s1.floorIndex(nums, target))

