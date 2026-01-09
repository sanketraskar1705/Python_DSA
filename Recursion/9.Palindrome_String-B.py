# Problem:- You are given a string s. Your task is to determine if the string is a palindrome.
# A string is considered a palindrome if it reads the same forwards and backwards.

# here ww use only one parameter that is string(s)

class Solution:
    def isPalindrome(self,s):

        # Base Case
        if len(s) <= 1:
            return True

        # If first and Last Character don't match
        if s[0] != s[-1]:
            return False

        ## Recursive call on remaining string
        return self.isPalindrome(s[1:-1])  # s[1:-1]  →  "iti"

s1 = Solution()
print(s1.isPalindrome('dhhlld'))
print(s1.isPalindrome('aba'))