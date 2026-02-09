# Binary Search to find X in sorted array
"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def binarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1      # move right
            else:
                high = mid - 1     # move left

        return -1


s1 = Solution()
nums = [-1, 23, 45, 77, 89, 90]
target = 89
print(s1.binarySearch(nums, target))

