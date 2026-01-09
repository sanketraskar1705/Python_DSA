# Problem:- You are given a string s. Your task is to determine if the string is a palindrome.
# A string is considered a palindrome if it reads the same forwards and backwards.
""" For check palindrome string we can use slicing but in this problem we solve problem using recursion"""
# Here we use left and right parameters

class Solution:
    def isPalindrome(self, s: str,left,right) -> bool:
        if left >= right:
            return True

        if s[left]!=s[right]:
            return False

        return self.isPalindrome(s,left+1,right-1)

s1=Solution()
print(s1.isPalindrome("nitin",0,4)) # here we give right index no. otherwise show "IndexError: string index out of range"