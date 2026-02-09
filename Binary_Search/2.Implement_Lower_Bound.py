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


"""
LOGIC EXPLANATION:

1. The goal is to find the index of the largest element
   in the sorted array that is less than or equal to target.
   This value is called the floor of the target.

2. Since the array is sorted, we use Binary Search
   to achieve O(log n) time complexity.

3. Initialize three variables:
   - low = 0 (starting index of array)
   - high = n - 1 (ending index of array)
   - ans = -1 (stores index of floor, default -1 if floor not found)

4. Run a loop while low <= high:
   - Compute mid = (low + high) // 2

5. If nums[mid] <= target:
   - This element can be the floor.
   - Store mid in ans.
   - Move RIGHT (low = mid + 1) to try finding a larger
     element still <= target (we need the largest floor).

6. Else (nums[mid] > target):
   - This element is greater than target.
   - Floor must lie on LEFT side.
   - Move LEFT (high = mid - 1).

7. When the loop finishes:
   - If ans == -1 → no element <= target exists in array.
   - Else → ans contains index of largest element <= target (floor index).

Time Complexity: O(log n)
Space Complexity: O(1)
"""


