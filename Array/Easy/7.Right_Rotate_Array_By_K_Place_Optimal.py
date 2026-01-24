# Problem :- Right rotate array by k place
# Optimal Solution

class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rightRotateArray(self, nums, k):
        n = len(nums)
        k = k % n   # handle k > n

        # Step 1: Reverse last k elements
        self.reverse(nums, n - k, n - 1)

        # Step 2: Reverse first n-k elements
        self.reverse(nums, 0, n - k - 1)

        # Step 3: Reverse whole array
        self.reverse(nums, 0, n - 1)

        return nums


# Example
s1 = Solution()
print(s1.rightRotateArray([3, 9, 5, 6, 7, 2, 10, 9], 5))

"""
1. Calculate k % n to handle cases where k is greater than the array length.
2. Reverse the last k elements of the array.
3. Reverse the first n - k elements of the array.
4. Reverse the entire array.
5. After these three reversals, the array becomes right-rotated by k places.

Time Complexity: O(n)
Space Complexity: O(1)
"""

