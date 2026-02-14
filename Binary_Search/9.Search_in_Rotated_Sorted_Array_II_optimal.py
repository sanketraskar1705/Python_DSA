# Problem :- Search in Rotated Sorted Array II
"""
Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.
"""
# Optimal Solution
class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # IMPORTANT: handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Right half sorted
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

            # Left half sorted
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False


s1 = Solution()
nums = [2,5,6,0,0,1,2]
target = 9
print(s1.search(nums, target))

"""
1. Goal:
   Search target in a rotated sorted array with duplicates.
   If found → return True
   If not found → return False

2. Initialize:
   low = 0, high = n-1

3. Run Binary Search while low ≤ high:
   - mid = (low + high) // 2

4. If nums[mid] == target:
   → target found → return True

------------------------------------------------------------

5. Handle duplicates (important case):

   If nums[low] == nums[mid] == nums[high]:
      → cannot determine sorted half
      → shrink search space
      → low += 1, high -= 1
      → continue

------------------------------------------------------------

6. Check which half is sorted:

   Case 1 → Right half is sorted (nums[mid] ≤ nums[high]):

      - If target lies in right half
        (nums[mid] ≤ target ≤ nums[high]):
            → search right → low = mid + 1
      - Else:
            → search left → high = mid - 1

------------------------------------------------------------

   Case 2 → Left half is sorted:

      - If target lies in left half
        (nums[low] ≤ target ≤ nums[mid]):
            → search left → high = mid - 1
      - Else:
            → search right → low = mid + 1

------------------------------------------------------------

7. If loop ends and target not found:
   → return False

------------------------------------------------------------

Time Complexity  :
   Average → O(log n)
   Worst (many duplicates) → O(n)

Space Complexity : O(1)
"""
