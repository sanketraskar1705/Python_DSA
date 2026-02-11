# Problem :-  Ceil The Floor
"""
You're given a sorted array 'a' of 'n' integers and an integer 'x'.
Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.
"""
# Optimal Solution
class Solution:
    def ceilFloor(self,nums,target):
        n = len(nums)
        floor = -1
        ceil = -1
        low, high =0 , n-1

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return [nums[mid],nums[mid]]
            elif nums[mid] > target:
                ceil = nums[mid]
                high = mid - 1
            else:
                floor = nums[mid]
                low = mid + 1
        return [floor,ceil]

s1 = Solution()
nums = [1,2,2,4,5,6,7,8,10,10]
target = 10
print(s1.ceilFloor(nums,target))

"""
1. Since the array is sorted, we can use Binary Search to find floor and ceil efficiently.

2. Initialize:
   floor = -1 (largest value ≤ target)
   ceil  = -1 (smallest value ≥ target)
   low = 0, high = n-1

3. Run Binary Search while low ≤ high:
   - Find mid = (low + high) // 2

4. If nums[mid] == target:
   - Target found → it is both floor and ceil
   - Return [nums[mid], nums[mid]]

5. If nums[mid] > target:
   - Current element can be a possible ceil
   - Store ceil = nums[mid]
   - Move left → high = mid - 1 (to find smaller possible ceil)

6. If nums[mid] < target:
   - Current element can be a possible floor
   - Store floor = nums[mid]
   - Move right → low = mid + 1 (to find larger possible floor)

7. When loop ends:
   - floor holds largest value ≤ target (or -1 if none)
   - ceil holds smallest value ≥ target (or -1 if none)

8. Return [floor, ceil]

Time Complexity  : O(log n)
Space Complexity : O(1)
"""