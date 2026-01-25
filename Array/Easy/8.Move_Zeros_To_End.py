# Problem :- Move zeros to end of list
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    def moveZeroes(self, arr):
        j = 0  # position for next non-zero

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

        return arr


s1 = Solution()
arr = [0,2,1,0,8,0,0,3,2,4]
print(s1.moveZeroes(arr))

"""
1. Use a pointer j to track the position where the next non-zero element should be placed.
2. Traverse the array using index i from start to end.
3. Whenever a non-zero element is found at index i, swap it with the element at index j.
4. Increment j after placing a non-zero element at its correct position.
5. This process keeps all non-zero elements in their original relative order and moves all zeros to the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""



