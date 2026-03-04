# Problem:- Excel Sheet Column Title
"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
"""
class Solution(object):
    def convertToTitle(self, columnNumber):
        result =""

        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            result = chr(remainder + ord("A")) + result
            columnNumber = columnNumber // 26

        return result

s1 = Solution()
columnNumber = 45
print(s1.convertToTitle(columnNumber))


"""
Logic of Excel Sheet Column Title Conversion

1. Excel column naming follows a 1-based base-26 system.
   Characters range from 'A' to 'Z' representing values 1 to 26.

2. Since modulo (%) works on 0-based indexing (0–25),
   we subtract 1 from columnNumber in every iteration
   to properly align it with 0-based indexing.

3. In each loop:
   - Find remainder using columnNumber % 26
     → This gives the current character position.
   - Convert remainder to corresponding uppercase letter
     using chr(remainder + ord('A')).
   - Append this character at the beginning of result
     because we are forming the string from right to left.
   - Divide columnNumber by 26 using integer division (//)
     to move to the next position.

4. The loop continues until columnNumber becomes 0.

Time Complexity:
O(log₍26₎ n)
Because in each iteration, columnNumber is divided by 26.

Space Complexity:
O(log₍26₎ n)
Because the result string stores one character per iteration."""