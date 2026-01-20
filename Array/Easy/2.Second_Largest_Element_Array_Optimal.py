# Problem :- Second largest element in array
# Optimal solution

class Solution:
    def secondLarge(self,arr):
        largest = float("-inf")
        s_largest = float("-inf")

        for i in range(0,len(arr)):
            if arr[i] > largest:
                s_largest = largest
                largest = arr[i]
            elif arr[i] > s_largest and arr[i] != largest :
                s_largest = arr[i]

        return s_largest

s1 = Solution()
arr=[34,12,256,32,43,665,77,54,9]
print(s1.secondLarge(arr))

"""
Logic:
1. Initialize two variables:
   - `largest` to store the largest element found so far.
   - `s_largest` to store the second largest element found so far.
   Both are initialized to negative infinity to safely handle
   arrays containing negative numbers.

2. Traverse the array only once (single pass):
   - If the current element is greater than `largest`:
     a) Assign the current `largest` value to `s_largest`
     b) Update `largest` with the current element
   - Else if the current element is:
     a) Greater than `s_largest`
     b) Not equal to `largest`
     then update `s_largest` with the current element

3. This ensures:
   - `largest` always holds the maximum value
   - `s_largest` always holds the biggest value smaller than `largest`

4. After completing the loop, return `s_largest`
   as the second largest element in the array.

5. Time Complexity: O(n)  
   Space Complexity: O(1)
"""
