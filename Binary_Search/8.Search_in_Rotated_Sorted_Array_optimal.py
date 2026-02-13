# Problem :- Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# Brute Solution

class Solution:
    def search(self, nums, target):
        n = len(nums)
        low ,high =0,n-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
            else:
                if nums[low] <= target<= nums[mid]:
                    high = mid -1
                else:
                    low = mid +1

        return -1

s1 = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(s1.search(nums, target))

"""
1. Goal:
   Search target in a rotated sorted array using Binary Search in O(log n).

2. Initialize:
   low = 0, high = n-1

3. Run Binary Search while low ≤ high:
   - mid = (low + high) // 2

4. If nums[mid] == target:
   → target found → return mid

------------------------------------------------------------

5. Check which half is sorted:

   Case 1 → Right half is sorted (nums[mid] ≤ nums[high]):

      - If target lies inside right sorted half
        (nums[mid] ≤ target ≤ nums[high]):
            → search right → low = mid + 1
      - Else:
            → search left → high = mid - 1

------------------------------------------------------------

   Case 2 → Left half is sorted (nums[mid] > nums[high]):

      - If target lies inside left sorted half
        (nums[low] ≤ target ≤ nums[mid]):
            → search left → high = mid - 1
      - Else:
            → search right → low = mid + 1

------------------------------------------------------------

6. If loop ends and target not found:
   → return -1

------------------------------------------------------------

Time Complexity  : O(log n)
Space Complexity : O(1)

"""
