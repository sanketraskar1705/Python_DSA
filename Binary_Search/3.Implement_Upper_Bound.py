""" Problem :-You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.
Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.
Note:
1. The upper bound in a sorted array is the index of the first value that is greater than a given value.
2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
3. Try to write a solution that runs in log(n) time complexity.
"""
# smallest index such that nums[i] > target

class Solution:
    def upperBound(self,nums,target):
        n = len(nums)
        ub = n
        low , high = 0,n-1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub

s1 = Solution()
nums = [2,4,6,7]
target = 5
print(s1.upperBound(nums,target))

"""
Logic :-

1. Upper bound means we need to find the smallest index i such that nums[i] > target.

2. Initialize:
   - low = 0 (start of array)
   - high = n-1 (end of array)
   - ub = n (default answer, if no element > target exists)

3. Use Binary Search (because array is sorted):

4. While low <= high:
      - Find mid = (low + high) // 2

      Case 1: nums[mid] > target
              → This index can be a possible upper bound.
              → Store ub = mid
              → But we want the FIRST such index, so search on LEFT side.
              → high = mid - 1

      Case 2: nums[mid] <= target
              → Upper bound must be on RIGHT side.
              → low = mid + 1

5. Loop ends when low > high.

6. Return ub:
      - If element greater than target exists → ub = index of first greater element.
      - If not → ub remains n (size of array).

Time Complexity  : O(log n)  
Space Complexity : O(1)
"""