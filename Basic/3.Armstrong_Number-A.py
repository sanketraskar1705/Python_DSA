# Python Program to Check Armstrong Number

class Solution:
    def isArmstrong(self,x)->bool:
        x = x
        num = x
        total = 0
        length = len(str(x))

        while num>0:
            ld = num % 10
            total = total+(ld ** length)
            num //= 10

        return x == total

s1=Solution()
print(s1.isArmstrong(123))
print(s1.isArmstrong(153))
