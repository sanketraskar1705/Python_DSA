# Problem :- Right rotate array by k place
# Brute Solution

class Solution:
    def rightRotateArray(self, arr, k):
        n = len(arr)
        rotations = k % n

        for i in range(rotations):
            e= arr.pop()
            arr.insert(0,e)

        return arr



s1 = Solution()

print(s1.rightRotateArray([1,2,3,4,5,6,7,8,9],3))


"""
1. Calculate the effective number of rotations using k % n to avoid unnecessary full rotations.
2. Perform the rotation process one step at a time.
3. In each rotation, remove the last element of the array.
4. Insert the removed element at the beginning of the array.
5. Repeat the process for the required number of rotations.
6. After all rotations, the array becomes right-rotated by k places.

Time Complexity: O(n * k)
Space Complexity: O(1)
"""

