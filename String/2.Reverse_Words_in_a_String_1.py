# Problem:- Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        rev= s[::-1]
        new_sentence = " ".join(rev)
        return new_sentence

s1 = Solution()
s = "the sky is blue"
print(s1.reverseWords(s))

"""
Logic:
1. Start the function and take string s as input.
2. Split the string into words using s.split() (removes extra spaces).
3. Reverse the list of words using slicing [::-1].
4. Join the reversed words with a single space using " ".join().
5. Return the final reversed sentence.

Time Complexity:
O(n) → Splitting, reversing, and joining process the whole string once.

Space Complexity:
O(n) → Extra space used for list of words and the new reversed string.
"""