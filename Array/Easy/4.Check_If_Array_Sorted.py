# Problem :- Check if array is sorted
# Given an array arr[], check whether it is sorted in non-decreasing order.
# Return true if it is sorted otherwise false.
# Optimal Solution

class Solution:
    def arraySorted(self,arr):
        n=len(arr)
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return False
        return True



s1 = Solution()
arr=[23,34,56,78,23]
print(s1.arraySorted(arr))


"""
1. Traverse the array from the first element to the second last element.
2. Compare each element with its next element.
3. If any element is greater than the next one, return False.
4. If no such case is found till the end, return True.
5. The array is checked in a single pass, making the solution optimal.
"""
