# Problem :- Print 1 to n No. Using Recursion
# Tail Recursion


class Solution:
    def isPrint(self,i,n):
        if i > n:
            return
        self.isPrint(i + 1, n)
        print(i)
        

s1=Solution()
s1.isPrint(1,4)