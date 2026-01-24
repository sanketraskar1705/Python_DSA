# Problem :- Right rotate array by k place
# Better Solution

class Solution:
    def rightRotateArray(self, arr, k):
        n = len(arr)

        if n == 0:
            return arr

        k = k % n  # IMPORTANT for n=2 and k>n
        arr[:] = arr[n-k:] + arr[:n-k]
        return arr

s1 = Solution()

print(s1.rightRotateArray([1,2,3,4,5,6,7,8,9],4))

"""
1. First check if the array is empty; if yes, return it as is.
2. Compute k % n to handle cases where k is greater than the array length.
3. Split the array into two parts:
   - Last k elements
   - First n - k elements
4. Concatenate the two parts in reversed order to achieve right rotation.
5. Update the original array using slicing.

Time Complexity: O(n)
Space Complexity: O(n)
"""
