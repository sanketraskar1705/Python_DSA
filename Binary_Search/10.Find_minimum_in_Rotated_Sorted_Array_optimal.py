# Problem:- Find minimum in Rotated Sorted Array
"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
# Optimal Solution

class Solution:
    def findMin(self,nums):
        n = len(nums)
        low,high=0,n-1
        mini = float("inf")
        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= nums[high]:
                mini = min(nums[mid],nums[high])
                high = mid - 1
            else:
                mini = min(nums[low],nums[mid])
                low = mid + 1
        return mini

s1 = Solution()
nums = [3,4,5,1,2]
print(s1.findMin(nums))

"""
Logic:
1. Start the function and take array nums as input.
2. Initialize low = 0 and high = n-1.
3. Initialize mini with infinity.
4. Run loop while low <= high.
5. Find mid = (low + high) // 2.
6. If right half (mid → high) is sorted:
      - Update mini with min(nums[mid], nums[high]).
      - Move search to left half → high = mid - 1.
7. Else left half (low → mid) is sorted:
      - Update mini with min(nums[low], nums[mid]).
      - Move search to right half → low = mid + 1.
8. Continue until loop ends.
9. mini contains the minimum element.
10. Return mini.

Time Complexity:
O(log n)  → Binary search halves the search space each step.

Space Complexity:
O(1)  → No extra space used (constant memory).
"""