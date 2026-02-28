# Problem :- Longest Palindromic Substring
class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd length palindrome
            l=r=i
            while l >= 0 and r <len(s) and s[l]==s[r]:
                if (r-l+1) > len(res):
                    res= s[l:r+1]
                l -= 1
                r += 1
            # even length palindrome
            while l >= 0 and r < len(s) and s[l]==s[r]:
                if (r-l+1) > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1

        return res

s1 = Solution()
s = "babad"
print(s1.longestPalindrome(s))

"""
Problem:
Find the longest palindromic substring in a given string.

Logic (Expand Around Center Approach):

1. Initialize an empty string 'res' to store the longest palindrome.

2. Traverse each index i in the string.
   Every character can act as a center of a palindrome.

3. For each index, check two cases:

   Case 1: Odd-length palindrome
   - Set l = i and r = i.
   - Expand outward while:
         l >= 0
         r < len(s)
         s[l] == s[r]
   - Update 'res' if current substring length is greater.

   Case 2: Even-length palindrome
   - Set l = i and r = i + 1.
   - Expand outward using the same condition.
   - Update 'res' if longer palindrome found.

4. Continue for all indices.

5. Return 'res' at the end.

Why This Works:
- A palindrome mirrors around its center.
- Every palindrome has either:
      • One center (odd length)
      • Two centers (even length)
- By expanding around each possible center, we check all palindromes.

Time Complexity:
- O(n^2) → For each character, we expand outward.

Space Complexity:
- O(1) → Only constant extra space used.
"""
