# Problem :- Smallest element in array

class Solution :
    def small(self,arr):
        min_val = arr[0]
        for i in range(1,len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]

        return min_val

s1= Solution()
arr=[23,4,1,5,65,43,54]
print(s1.small(arr))


"""
Logic:
1. Assume the first element of the array as the smallest element
   and store it in `min_val`.

2. Start iterating from the second element (index 1),
   since the first element is already considered.

3. For each element in the array:
   - Compare the current element with `min_val`.
   - If the current element is smaller than `min_val`,
     update `min_val` with this value.

4. Continue this process until the end of the array.

5. After the loop completes, `min_val` will contain
   the smallest element present in the array.

6. Return `min_val` as the smallest element.
"""
