# Problem :- Number of Digits
# Ninja want to add coding to his skill set so he started learning it. On the first day,
# he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.


class Solution:
    def countDigits(self,x: int ) -> int:
        cd = len(str(abs(x)))
        cd = int(cd)
        return cd

s1=Solution()
print(s1.countDigits(0))