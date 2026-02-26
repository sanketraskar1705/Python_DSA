# Problem :- Maximum Nesting Depth of the Parentheses
"""
Given a valid parentheses string s, return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses.
"""
class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        cur_depth = 0

        for bracket in s:
            if bracket == "(":
                cur_depth += 1
                max_depth = max(max_depth,cur_depth)
            elif bracket == ")":
                cur_depth -= 1

        return max_depth

s1 = Solution()
s ="(3+4(65*2(34-1)(34%6)))"
print(s1.maxDepth(s))

"""
Problem:
Find the maximum nesting depth of parentheses in a valid string.

Logic:

1. Initialize two variables:
   - cur_depth → keeps track of current open parentheses count.
   - max_depth → stores the maximum depth reached so far.

2. Traverse each character in the string:
   - If the character is '(':
        • Increase cur_depth by 1.
        • Update max_depth using:
              max_depth = max(max_depth, cur_depth)
   - If the character is ')':
        • Decrease cur_depth by 1.

3. Since the string is valid:
   - cur_depth will never go negative.
   - At the end, cur_depth will return to 0.

4. Return max_depth as the final answer.

Time Complexity:
- O(n), because we traverse the string once.

Space Complexity:
- O(1), because we only use two integer variables.
"""
