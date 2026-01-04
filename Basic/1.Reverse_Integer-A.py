# Leetcode #7 : Reverse Integer Python Program Explained
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self,x):
        sign = -1 if x<0 else 1                 # if int x is small then this is -1 else 1 // this Ternary Operator or Conditional Expression in one line code
        x= abs(x)       # Remove - sign

        result = sign * int(str(x)[::-1])       # here we convert int into str then use list slicing and reverse list and again convert it into int multiply with sign variable

        if -2**31 <= result <= 2**31-1:
            return result

        return 0

s1 = Solution()
print(s1.reverse(123))
print(s1.reverse(-345))