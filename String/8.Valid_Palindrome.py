# Problem:- 125. Valid Palindrome
""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise. """

class Solution(object):
    def isPalindrome(self, s):
        result =""

        for ch in s :
            if ch.isalnum():
                result += ch.lower()

        return result == result[::-1]

s1 = Solution()
s="A man, a plan, a canal: Panama"
print(s1.isPalindrome(s))