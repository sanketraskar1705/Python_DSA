# Problem :- Print 1 to n No. Using Recursion
# Head Recursion

class Solution:
    def isPrint(self,i,n):

        if i>n:
            return

        print(i)
        self.isPrint(i+1,n)

s1=Solution()
s1.isPrint(6,8)
