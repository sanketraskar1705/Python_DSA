# This is division logic

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = reverse * 10 + x % 10
            x //= 10

        return reverse == xcopy

s1=Solution()
print(s1.isPalindrome(123))
print(s1.isPalindrome(-123))
print(s1.isPalindrome(323))