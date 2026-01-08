# Problem:- Sum of 1 to n

class Solution:
    def isSum(self,sum,i,n):
        if i > n:
            print(sum)
            return

        self.isSum(sum+i,i+1,n)

s1=Solution()
s1.isSum(0,1,10)