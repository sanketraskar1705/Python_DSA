# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.



class Solution:
    def ispalindrome(self,x):

        return str(x)== str(x)[::-1]


s1=Solution()
print(s1.ispalindrome(123))
print(s1.ispalindrome(323))
print(s1.ispalindrome(-323))
