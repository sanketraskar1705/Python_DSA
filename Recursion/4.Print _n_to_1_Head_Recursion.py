# Problem :- Print n to 1 no. using recursion
# Head Recursion

class Solution:
    def isPrint(self,n):

        if n < 1:
            return

        print(n)
        self.isPrint(n-1)

s1=Solution()
s1.isPrint(7)

