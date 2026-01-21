# Problem:- Second smallest elements in array
# Better Solution
class Solution:
    def second_small(self,arr):
        smallest = float('inf')
        s_smallest = float('inf')

        for i in range(len(arr)):
            smallest = min(arr[i],s_smallest)

        for i in range(len(arr)):
            if arr[i] < s_smallest and arr[i] != smallest:
                s_smallest = arr[i]

        return s_smallest


s1 = Solution()
arr=[34,12,256,32,43,665,77,54,9]
print(s1.second_small(arr))


"""
Logic (Intended Approach for Second Smallest Element):

1. Initialize two variables:
   - `smallest` to store the smallest element in the array.
   - `s_smallest` to store the second smallest element.
   Both are initialized with positive infinity to handle
   arrays with large or negative values safely.

2. First traversal of the array:
   - Compare each element with `smallest`.
   - Update `smallest` whenever a smaller value is found.
   After this loop, `smallest` should contain
   the minimum element of the array.

3. Second traversal of the array:
   - Check each element.
   - Update `s_smallest` only if:
     a) The element is smaller than `s_smallest`
     b) The element is NOT equal to `smallest`
   This ensures we find the smallest value
   greater than `smallest`.

4. After the second loop, `s_smallest` will store
   the second smallest element in the array.

5. Return `s_smallest` as the final answer.
   (If no second smallest exists, it will remain `inf`.)

Note:
- This is a two-pass (better) solution.
- Time Complexity: O(n)
- Space Complexity: O(1)
"""
