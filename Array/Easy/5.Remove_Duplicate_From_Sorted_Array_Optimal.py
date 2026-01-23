# Problem :- Remove duplicate from sorted array
# Optimal Solution

class Solution:
    def removeDuplicates(self, arr):
        n=len(arr)
        if n ==1:
            return 1

        i =0
        j= i+1

        while j < n:
            if arr[i] != arr[j]:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]

            j +=1

        return i+1

s1= Solution()
arr= [1,1,2,3,3,3,4,5,5,6,7]
lenght = s1.removeDuplicates(arr)
print(f"{lenght}",end=",")
print(arr[:lenght])


"""
1. Use two pointers where pointer i tracks the position of the last unique element.
2. Initialize i at index 0 and j at index 1 to start comparison.
3. Traverse the array using pointer j.
4. When arr[i] is not equal to arr[j], it means a new unique element is found.
5. Increment pointer i and place the unique element at position i.
6. Continue this process until the end of the array.
7. The number of unique elements is i + 1.
8. The first i + 1 elements of the array contain the result without duplicates.

Time Complexity: O(n)
Space Complexity: O(1)
"""

