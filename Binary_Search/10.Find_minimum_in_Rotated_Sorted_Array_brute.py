# Problem:- Find minimum in Rotated Sorted Array
"""
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
# Brute Solution
class Solution:
    def findMin(self,nums):
        n = len(nums)
        mini_value = float("inf")
        for i in range(0,n):
            mini_value =min(nums[i],mini_value)
        return mini_value

s1 = Solution()
nums=[1,2,3,4,5]
print(s1.findMin(nums))

"""
Logic:
1. Start the function and take array nums as input.
2. Initialize mini_value with infinity.
3. Traverse the array from index 0 to n-1.
4. Compare each element nums[i] with mini_value.
5. If nums[i] is smaller, update mini_value.
6. Continue until all elements are checked.
7. After traversal, mini_value holds the minimum element.
8. Return mini_value.

Time Complexity:
O(n)  → because we traverse the entire array once.

Space Complexity:
O(1)  → no extra space is used (constant memory).
"""