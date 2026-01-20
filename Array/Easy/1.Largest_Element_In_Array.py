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
