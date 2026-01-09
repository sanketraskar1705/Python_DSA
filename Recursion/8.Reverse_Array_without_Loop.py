# Problem :- Given an array arr, you need to reverse a subarray of that array.
# The range of this subarray is given by indices l and r (1-based indexing).

class Solution:
    def reverseArray(self,arr,l,r) ->list:

        if l>=r:
            return arr

        arr[l],arr[r]=arr[r],arr[l]
        return self.reverseArray(arr,l+1,r-1)

s1=Solution()
print(s1.reverseArray([1,2,3,4,5,6,7,8,9],4,7))

#aa=[ 1,2,3,4,5,6,7,8,9]

#print(aa[2:])

#print(aa[:2:-1])