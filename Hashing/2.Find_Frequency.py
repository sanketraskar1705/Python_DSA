# Problem :- Given an array arr of positive integers and an integer x. Return the frequency of x in the array.

class Solution:
    def freCount(self,arr,x):
        count = 0
        for i in arr:
            if i == x:
                count += 1

        return count

s1= Solution()
print(s1.freCount([2,4,5,2,1,6,6,8,2,4,3,],2))