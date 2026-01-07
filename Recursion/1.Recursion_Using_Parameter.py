# Problem :- Print x with n times

class Solution:
    def isPrint(self,x,n):

        if n ==0:
            return
        print(x)
        self.isPrint(x,n-1)

s1=Solution()
s1.isPrint(15,5)