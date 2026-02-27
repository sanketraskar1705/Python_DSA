# Problem :- Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        letters ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(s)
        result = 0
        for i in range(0,n):
            if i <n-1 and letters[s[i]] < letters[s[i+1]]:
                result -= letters[s[i]]
            else:
                result += letters[s[i]]

        return result

s1 =Solution()
s = "LVIII"
print(s1.romanToInt(s))

"""
Problem:
Convert a Roman numeral string into its corresponding integer value.

Logic:

1. Create a dictionary that maps each Roman symbol to its integer value.

2. Initialize a variable 'result' to store the final number.

3. Traverse the string from left to right.

4. For each character at index i:
   - If it is NOT the last character
   - AND the value of current symbol is less than the value of the next symbol,
        → subtract its value from result.
   - Otherwise,
        → add its value to result.

5. Why subtraction?
   In Roman numerals, when a smaller value appears before a larger value,
   it means subtraction (e.g., IV = 5 - 1).

6. Continue until the end of the string.

7. Return the final result.

Time Complexity:
- O(n), since we traverse the string once.

Space Complexity:
- O(1), because the dictionary size is constant (7 symbols).
"""