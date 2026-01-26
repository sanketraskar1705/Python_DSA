# problem :- Find missing number in list
# Better Solution

class Solution:
    def  findElement(self,arr):
        n = len(arr)
        freq = { }

        for i in range(n+1):
            freq[i] = 0

        for i in range(n):
            freq[arr[i]] = 1

        for k,v in freq.items():
            if v == 0 :
                return k

s1= Solution()
arr = [0,2,1,3]
print(s1.findElement(arr))