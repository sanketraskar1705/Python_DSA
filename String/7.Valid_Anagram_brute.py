# Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
# Brute Solution
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False

s1 = Solution()
s="rat"
t="tar"
print(s1.isAnagram(s,t))
"""
Algorithm / Logic : Valid Anagram

1. Start

2. Create a function isAnagram(s, t)

3. Check length of both strings
   If len(s) != len(t)
       return False

4. Sort both strings
       sorted_s = sorted(s)
       sorted_t = sorted(t)

5. Compare sorted strings
       If sorted_s == sorted_t
            return True
       Else
            return False

6. End


Time Complexity:
Sorting each string takes O(n log n)
Total Time Complexity = O(n log n)

Space Complexity:
Extra space used for sorted strings
Space Complexity = O(n)
"""
