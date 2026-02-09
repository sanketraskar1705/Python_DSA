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

"""
LOGIC EXPLANATION:

1. The goal is to find the index of the target element
   in a sorted array using Binary Search.

2. Since the array is sorted, Binary Search allows us
   to reduce the search space by half each time,
   giving O(log n) time complexity.

3. Initialize two pointers:
   - low = 0 (start of array)
   - high = n - 1 (end of array)

4. Run a loop while low <= high:
   - Find mid = (low + high) // 2

5. If nums[mid] == target:
   - Target found at index mid.
   - Return mid.

6. Else if nums[mid] < target:
   - Target must be on the RIGHT side.
   - Move RIGHT (low = mid + 1).

7. Else (nums[mid] > target):
   - Target must be on the LEFT side.
   - Move LEFT (high = mid - 1).

8. If the loop ends without finding target:
   - Target does not exist in array.
   - Return -1.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
