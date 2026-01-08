# Problem :- Factorial of a number

class Solution:
    def factorial(self,num):

        if num == 0 or num == 1:
            return 1

        return num * (self.factorial(num-1))

s1=Solution()
print(s1.factorial(5))