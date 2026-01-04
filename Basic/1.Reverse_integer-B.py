# Reverse integer using division by 10

class Solution:
    def reverse(self,x):
        rev = 0

        sign = -1 if x<0 else 1         # Ternary operator
        x=abs(x)                        # Remove - sign

        while x>0:
            rev = rev * 10 + x % 10     # Multiply rev by 10 to shift digits, then add last digit of x
            x //=10                     # // is floor division (integer division)   It divides and removes the decimal part.

        return sign*rev

s1= Solution()
print(s1.reverse(123))
print(s1.reverse(-8597))