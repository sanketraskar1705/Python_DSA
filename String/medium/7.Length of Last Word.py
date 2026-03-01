#Problem :- Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        n=len(s)

        for i in range(n-1,-1,-1):

            # skip trailing spaces
            if s[i] == " " and length == 0:
                continue

            # if space found after counting started,stop
            if s[i] == " ":
                break

            # count characters
            length +=1

        return length

s1 = Solution()
s = "Hello World  "
print(s1.lengthOfLastWord(s))

"""
Problem: Length of Last Word

Step 1:
Initialize length = 0.
This variable will store the length of the last word.

Step 2:
Store the length of the string using:
n = len(s)

Step 3:
Traverse the string from right to left
using:
for i in range(n-1, -1, -1)

Step 4:
If the current character is a space AND
we have not started counting yet (length == 0),
it means we are skipping trailing spaces.
So, use continue.

Step 5:
If the current character is a space AND
we have already started counting (length > 0),
it means the last word has ended.
So, break the loop.

Step 6:
If the character is not a space,
increment length by 1.
This counts characters of the last word.

Step 7:
Return length.
This gives the length of the last word.


Time Complexity:
O(n)
Because in the worst case, we may traverse the entire string once.

Space Complexity:
O(1)
Because we are using only a few variables (length, n, i)
and no extra data structures.
"""