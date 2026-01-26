# Problem :- Union of sorted array

class Solution:
    def mergeTwoLists(self, arr1, arr2):
        res = []
        n = len(arr1)
        m = len(arr2)
        i = j = 0

        while i < n and j < m:
            if arr1[i] <= arr2[j]:
                if len(res) == 0 or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i+=1
            else:
                    if len(res) == 0 or res[-1] != arr2[j]:
                        res.append(arr2[j])
                    j+=1

        while i< n:
            if len(res) == 0 or res[-1] != arr1[i]:
                res.append(arr1[i])
            i+=1

        while j< m:
            if len(res) == 0 or res[-1] != arr2[j]:
                res.append(arr2[j])
            j+=1

        return res


s1  = Solution()
arr1 = [1,2,2,2,3,4,4,5]
arr2 = [1,1,2,3,3,3,4,5,6,7,8,8,9,10,10]
print(s1.mergeTwoLists(arr1, arr2))

