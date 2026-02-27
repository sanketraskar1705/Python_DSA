# Problem :- String  to  integer
"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
"""
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()

        if not s:
            return 0
        sign =1
        result = 0

        if s[0]=="-" or s[0]=="+":
            if s[0] ==  "-":
                sign = -1
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break
            result = result *10 + int(char)

        result *= sign

        if result < -2**31:
            return -2**31
        elif result > 2**31-1:
            return 2**31-1

        return result

s1 = Solution()
s = "1337c0d3"
print(s1.myAtoi(s))

"""
Problem:
Convert a string into a 32-bit signed integer following specific rules.

Logic:

Step 1: Remove Leading Whitespace
- Use strip() to remove leading and trailing spaces.
- If the string becomes empty, return 0.

Step 2: Handle Sign
- Initialize sign = 1.
- If the first character is '+' or '-':
      • If '-', set sign = -1.
      • Remove the sign character from the string.

Step 3: Convert Characters to Integer
- Initialize result = 0.
- Traverse each character in the string:
      • If the character is not a digit, stop the loop.
      • Otherwise, update result using:
            result = result * 10 + int(char)
  (This shifts digits left and adds the new digit.)

Step 4: Apply Sign
- Multiply result by sign.

Step 5: Handle 32-bit Integer Overflow
- The valid range is:
      [-2^31, 2^31 - 1]
- If result is smaller than -2^31, return -2^31.
- If result is greater than 2^31 - 1, return 2^31 - 1.

Step 6: Return Final Result

Time Complexity:
- O(n), where n is length of string (single traversal).

Space Complexity:
- O(1), only constant extra variables used.
"""
