# Problem :- Second largest element in array
# Better solution
class Solution:
    def secondLarge(self,arr):
        largest = float('-inf')
        s_largest = float('-inf')
        n = len(arr)

        for i in range(n):
            largest = max(arr[i],largest)

        for i in range(0,n):
            if arr[i] > s_largest and arr[i] != largest:
                s_largest = arr[i]

        return s_largest


s1 = Solution()
arr=[34,12,256,32,43,665,77,54,9]
print(s1.secondLarge(arr))

"""
Logic:
1. Initialize two variables:
   - `largest` to store the maximum element in the array.
   - `s_largest` to store the second largest element.
   Both are initialized with negative infinity to handle negative values safely.

2. Traverse the array for the first time:
   - Compare each element with `largest`.
   - Update `largest` whenever a bigger element is found.
   After this loop, `largest` contains the maximum element of the array.

3. Traverse the array for the second time:
   - Check each element.
   - Update `s_largest` only if:
     a) The element is greater than `s_largest`
     b) The element is NOT equal to `largest`
   This ensures we find the biggest element smaller than `largest`.

4. Return `s_largest` as the second largest element in the array.
   - If no such element exists, it will remain `-inf` (can be handled separately if needed).
"""
