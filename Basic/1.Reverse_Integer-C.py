class Solution:
    def reverse(self,x):
        x=str(x)

        if x[0]=='-':
            rev= '-'+x[:0:-1]
        else:
            rev = x[::-1]

        num = int(rev)

        if -2**31 <= num <= 2**31-1:
            return num

        return 0

s1=Solution()
print(s1.reverse(123))
print(s1.reverse(-9798))