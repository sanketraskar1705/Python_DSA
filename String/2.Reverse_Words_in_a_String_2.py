# Problem:- Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        result =[]
        i = len(s)-1

        while i >= 0 :
            while  i >= 0 and s[i]==" ":
                i -=1
            if i < 0:
                break
            j = i
            while i >= 0  and s[i] !=" ":
                i -= 1

            result.append(s[i+1:j+1])

        return " ".join(result)


s1 = Solution()
s = "the sky is blue"
print(s1.reverseWords(s))

"""Logic:
1. Start the function and take string s as input.
2. Initialize empty list result to store reversed words.
3. Set pointer i at the end of the string (len(s) - 1).
4. Skip all trailing spaces by moving i left.
5. If i becomes < 0, stop the process.
6. Mark j = i as the end of the current word.
7. Move i left until a space is found → this gives the start of the word.
8. Extract the word using s[i+1 : j+1] and append to result.
9. Repeat steps 4–8 until the whole string is processed.
10. Join words in result with a single space using " ".join().
11. Return the reversed sentence.

Time Complexity:
O(n) → Each character is processed at most once.

Space Complexity:
O(n) → Extra space used to store the result words and final string.

"""