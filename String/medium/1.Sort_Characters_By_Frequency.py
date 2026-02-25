# Problem :- Sort Characters By Frequency

class Solution:
    def frequencySort(self, s):
        result = " "
        hash_map = { }

        for ch in s :
            hash_map[ch]=hash_map.get(ch,0)+1

        sorted_char=sorted(hash_map.items(),key=lambda x: (-x[1],x[0]))

        for ch,freq in sorted_char:
            result += ch * freq

        return result

s1 = Solution()
s= "tree"
print(s1.frequencySort(s))

"""
Problem:
Sort the characters of a string in decreasing order based on their frequency.

Step 1: Count Frequency
- Create an empty dictionary (hash_map).
- Traverse each character in the string.
- For every character, update its count using:
      hash_map[ch] = hash_map.get(ch, 0) + 1

Step 2: Sort the Characters
- Convert the dictionary into (character, frequency) pairs using items().
- Sort them using:
      key = lambda x: (-x[1], x[0])

Explanation of sorting:
- x[1] represents frequency.
- -x[1] ensures sorting in descending order of frequency.
- x[0] ensures alphabetical order when frequencies are equal.

Step 3: Build the Result String
- For each (character, frequency) pair:
      repeat the character 'frequency' times.
- Concatenate all repeated characters to form the final string.

Time Complexity:
- Frequency counting → O(n)
- Sorting → O(k log k), where k = number of unique characters
- Building result → O(n)

Overall Complexity → O(n log k)
"""