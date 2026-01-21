# Problem :- Large Small Second Large Second Small

class Solution:
    def getSecondOrderElements(self, a: [int]) -> [int]:
        largest = float("-inf")
        s_largest = float("-inf")
        smallest = float("inf")
        s_smallest = float("inf")

        for i in range(len(a)):

            # Second largest
            if a[i] > largest:
                s_largest = largest
                largest = a[i]
            elif a[i] > s_largest and a[i] != largest:
                s_largest = a[i]

            # Second smallest
            if a[i] < smallest:
                s_smallest = smallest
                smallest = a[i]
            elif a[i] < s_smallest and a[i] != smallest:
                s_smallest = a[i]

        return [s_largest, s_smallest]

s1 = Solution()
a=[23,45,7,65,98,82,53,5,73,989]
print(s1.getSecondOrderElements(a))


"""
Logic:
1. Initialize four variables:
   - `largest` to store the largest element found so far.
   - `s_largest` to store the second largest element.
   - `smallest` to store the smallest element found so far.
   - `s_smallest` to store the second smallest element.
   `largest` and `s_largest` are initialized with -infinity,
   while `smallest` and `s_smallest` are initialized with +infinity
   to handle all possible integer values safely.

2. Traverse the array only once (single pass):
   For each element `a[i]`, perform two independent checks:

   a) Second Largest Logic:
      - If the current element is greater than `largest`:
        i) Move the current `largest` value to `s_largest`
        ii) Update `largest` with the current element
      - Else if the current element is:
        i) Greater than `s_largest`
        ii) Not equal to `largest`
        then update `s_largest`

   b) Second Smallest Logic:
      - If the current element is smaller than `smallest`:
        i) Move the current `smallest` value to `s_smallest`
        ii) Update `smallest` with the current element
      - Else if the current element is:
        i) Smaller than `s_smallest`
        ii) Not equal to `smallest`
        then update `s_smallest`

3. By the end of the loop:
   - `largest` holds the maximum value
   - `s_largest` holds the second largest value
   - `smallest` holds the minimum value
   - `s_smallest` holds the second smallest value

4. Return the result as a list:
   `[second_largest, second_smallest]`

5. Time Complexity: O(n)  
   Space Complexity: O(1)
"""

