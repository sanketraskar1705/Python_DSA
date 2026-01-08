# Problem :- Given an integer n, calculate the sum of series 1**3 + 2**3 + 3**3 + 4**3 + … till n-th term.

class Solution:
    def sumCube(self,n):
        if n==0 or n==1:
            return 1

        return n**3 +self.sumCube(n-1)

s1=Solution()
print(s1.sumCube(5))