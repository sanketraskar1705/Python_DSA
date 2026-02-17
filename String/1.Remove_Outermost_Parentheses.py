#Problem :- Remove Outermost Parentheses

class Solution:
    def removeParentheses(self,s):
        result = ""
        count = 0
        for ch in s:
            if ch == "(":
                count += 1
                if count > 1:
                    result += ch
            else:
                count -= 1
                if count > 0:
                    result += ch
        return result

s1 = Solution()
str1 = "(()())(())"
print(s1.removeParentheses(str1))
str2 = "(()())(())(()(()))"
print(s1.removeParentheses(str2))

"""
Logic:
1. Start the function and take string s as input.
2. Initialize empty string result to store answer.
3. Initialize count = 0 to track parentheses depth.
4. Traverse each character ch in string s.
5. If ch == "(":
      - Increase count by 1.
      - If count > 1, add "(" to result (skip outermost).
6. Else ch == ")":
      - Decrease count by 1.
      - If count > 0, add ")" to result (skip outermost).
7. Continue until all characters are processed.
8. Return result string after removing outermost parentheses.

Time Complexity:
O(n) → We traverse the string once.

Space Complexity:
O(n) → Result string stores up to n characters.
"""