# Problem:- Second smallest elements in array
# Optimal Solution

class Solution:
    def second_smaller(self, arr):
        smallest = float('inf')
        s_smallest = float('inf')

        for i in range(len(arr)):
            if arr[i] < smallest:
                s_smallest = smallest
                smallest = arr[i]
            elif arr[i] < s_smallest and arr[i] != smallest:
                s_smallest = arr[i]

        return s_smallest

s1 = Solution()
arr=[34,12,256,32,43,665,77,54,9]
print(s1.second_smaller(arr))

"""
Logic:
1. Initialize two variables:
   - `smallest` to keep track of the smallest element found so far.
   - `s_smallest` to keep track of the second smallest element.
   Both are initialized with positive infinity so that any element
   in the array can replace them during comparison.

2. Traverse the array only once (single pass):
   - If the current element is smaller than `smallest`:
     a) Assign the current value of `smallest` to `s_smallest`
     b) Update `smallest` with the current element
   - Else if the current element is:
     a) Smaller than `s_smallest`
     b) Not equal to `smallest`
     then update `s_smallest` with the current element

3. This guarantees:
   - `smallest` always stores the minimum element
   - `s_smallest` always stores the smallest value
     greater than `smallest`

4. After completing the loop, return `s_smallest`
   as the second smallest element in the array.

5. Time Complexity: O(n)  
   Space Complexity: O(1)
"""
