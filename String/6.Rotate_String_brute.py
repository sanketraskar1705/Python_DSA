# Problem :- 796. Rotate String
"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
"""
# Brute Force Solution

class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        cur_s = s
        n = len(cur_s)
        for i in range(0,n):
            if cur_s == goal:
                return True
            cur_s = cur_s[-1]+cur_s[:-1]

        return False

s1 = Solution()
s = "abcde"
goal = "cdeab"
print(s1.rotateString(s,goal))

"""
Logic:

1. If lengths of s and goal are different → return False.

2. Store the original string in cur_s.

3. Repeat rotation n times (n = length of string).

4. In each iteration:
   - Check if cur_s == goal → return True.
   - Perform one rotation by moving last character to front.

5. Continue until all rotations are checked.

6. If goal is not matched after all rotations → return False.


Complexity:

Time Complexity  : O(n²)  
Space Complexity : O(n)
"""
