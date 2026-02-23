# Problem :- 796. Rotate String
"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""
# Optimal Solution

class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        double_s = s+s
        if goal in double_s:
            return True
        return False
s1 =Solution()
s = "abcde"
goal = "cdeab"
print(s1.rotateString(s,goal))

"""
Logic:

1. If lengths of s and goal are not equal → return False.

2. Create a new string by concatenating s with itself:
   double_s = s + s

3. If goal is a substring of double_s → return True.

4. Otherwise → return False.


Complexity:

Time Complexity  : O(n)  
→ String concatenation + substring check.

Space Complexity : O(n)  
→ Extra space used for double_s.
"""