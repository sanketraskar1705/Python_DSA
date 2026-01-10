# Problem:- Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
# such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
from pickletools import string1


class Solution:
    def fibonacci(self, n: int) -> int:
        if n==0 or n==1:
            return n

        return self.fibonacci(n-1) + self.fibonacci(n-2)

s1=Solution()
print(s1.fibonacci(10))