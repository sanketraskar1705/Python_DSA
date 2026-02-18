# Problem :- Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

s1 =Solution()
strs = ["flower","flow","flight"]
print(s1.longestCommonPrefix(strs))

"""
Logic:

1. We need to find the longest common prefix (starting characters) shared by all strings.

2. Take the first string as reference (strs[0]) because the prefix must match it.

3. Start checking characters index by index (from left to right).

4. For each index i in first string:
   - Compare the character strs[0][i] with the character at index i in every other string.
   - If any string ends (i == len(s)) OR characters do not match → stop and return current prefix.

5. If all strings have the same character at index i:
   - Add that character to result (res).

6. Continue until mismatch occurs or end of first string reached.

7. If loop finishes → return res (full prefix).
Complexity:

Time Complexity  : O(n * m)  
→ n = number of strings  
→ m = length of smallest string  
(We may compare each character of each string once)

Space Complexity : O(1)  
→ Only constant extra space used (result string not counted).
"""