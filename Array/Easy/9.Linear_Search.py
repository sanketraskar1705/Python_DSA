# Problem :- Linear search of element in array and return index of it, if element not present in array

class Solution:
    def search(self,arr,target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

s1 = Solution()
arr =[23,45,12,3,53,78,20]
target = 45
print(s1.search(arr,target))


"""
1. Traverse the array from the first element to the last element.
2. Compare each element with the target value.
3. If the target value matches the current element, return its index immediately.
4. If the loop completes and the target is not found, return -1.
5. This method checks elements one by one, following a linear search approach.

Time Complexity: O(n)
Space Complexity: O(1)
"""
