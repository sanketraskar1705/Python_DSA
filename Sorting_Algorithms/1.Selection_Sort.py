# Selection Sort

class Solution:
    def selction(self,arr):

        for i in range(len(arr)):
            min_val = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[min_val]:
                    min_val = j

            arr[i],arr[min_val] = arr[min_val],arr[i]

        return arr

s1=Solution()
print(s1.selction([23,42,1,3,21,86,23,97,53,34,22,19]))
