# Problem :- Largest Elements In Array

class Solution:
    def largestEle(self,arr):
        mix_val=arr[0]
        for i in range(1,len(arr)):
            if arr[i] > mix_val:
                mix_val=arr[i]

        return mix_val

s1=Solution()
arr=[2,3,1,3,4,5,6]
print(s1.largestEle(arr))

"""
Logic:
1. Assume the first element of the array as the largest element
   and store it in `mix_val`.

2. Start traversing the array from index 1 (second element),
   because index 0 is already considered.

3. For each element:
   - Compare the current element with `mix_val`.
   - If the current element is greater than `mix_val`,
     update `mix_val` with this value.

4. After completing the loop, `mix_val` will contain
   the largest element present in the array.

5. Return `mix_val` as the largest element.
"""

