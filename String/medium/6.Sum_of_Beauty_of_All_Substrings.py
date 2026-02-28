# Problem :- Sum of Beauty of All Substrings
"""
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.
"""

class Solution(object):
    def beautySum(self, s):
        n = len(s)
        total = 0

        for i in range(n):
            freq = [0]*26
            max_freq = 0

            for j in range(i,n):
                index = ord(s[j]) - ord("a")
                freq[index] += 1
                # update max frequency dynamically
                max_freq = max(max_freq,freq[index])
                # compute min frequency among non-zero characters
                min_freq =float('inf')
                for f in freq:
                    if f > 0:
                        min_freq = min(min_freq,f)

                total += (max_freq-min_freq)

        return total

s1 = Solution()
s = "aabcb"
print(s1.beautySum(s))


"""
Problem:
For every substring of a string, compute its beauty.
Beauty = (maximum character frequency - minimum character frequency among non-zero characters).
Return the sum of beauty of all substrings.

Logic:

1. Initialize:
   - total = 0 → stores final answer.
   - n = length of string.

2. Fix the starting index 'i' of substring.
   - For each i, create a frequency array of size 26 (for lowercase letters).
   - Initialize max_freq = 0.

3. Extend substring using ending index 'j' from i to n-1:
   - Update frequency of current character.
   - Dynamically update max_freq.
   - Compute min_freq by checking all non-zero frequencies in freq array.
   - Beauty of current substring = max_freq - min_freq.
   - Add this beauty to total.

4. Repeat for all starting indices.

5. Return total.

Why This Works:
- Instead of generating substrings separately,
  we expand each substring incrementally.
- Frequency array avoids recomputing counts from scratch.
- max_freq is updated dynamically.
- min_freq is computed from only 26 letters (constant work).

Time Complexity:
- Outer loop → O(n)
- Inner loop → O(n)
- Min frequency scan → O(26)
Overall → O(n²)

Space Complexity:
- O(26) → constant space for frequency array.
"""