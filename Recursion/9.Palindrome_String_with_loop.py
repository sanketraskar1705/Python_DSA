class Solution:
    def isPalindrome(self,s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

s1=Solution()
print(s1.isPalindrome("dhjfdfh"))
print(s1.isPalindrome("nitin"))
