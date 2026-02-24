# Valid Anagram
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""
# Brute Solution
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = { }

        for ch in s:
            count[ch]=count.get(ch,0)+1

        for ch in t:
            if ch not in count or count[ch]==0:
                return False
            count[ch] -= 1
        return True

s1 =Solution()
s="rat"
t="bat"
print(s1.isAnagram(s,t))

"""
Algorithm / Logic : Valid Anagram (HashMap Approach)

1. Start

2. Create a function isAnagram(s, t)

3. Check the length of both strings
   If len(s) != len(t)
       return False

4. Create an empty dictionary called count
   This will store frequency of characters.

5. Traverse string s
   For each character ch in s
       count[ch] = count.get(ch, 0) + 1

6. Traverse string t
   For each character ch in t
       If ch not in count OR count[ch] == 0
           return False
       Otherwise decrease the count
           count[ch] -= 1

7. If all characters matched
       return True

8. End


Time Complexity:
O(n)
We traverse both strings once.

Space Complexity:
O(1) for fixed alphabet (or O(k) where k is number of unique characters).
"""