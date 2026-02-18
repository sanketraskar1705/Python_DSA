# Problem:- Isomorphic Strings
class Solution(object):
    def isIsomorphic(self, s, t):
        map_st,map_ts= {},{}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # s -> t check
            if char_s in map_st:
                if map_st[char_s] != char_t:
                    return False
                else:
                    map_st[char_s] = char_t

            # t -> s check
            if char_t in map_ts:
                if map_ts[char_t] != char_s:
                    return False
                else:
                    map_ts[char_t] = char_s

        return  True

s1 = Solution()
s = "egg"
t = "add"
print(s1.isIsomorphic(s,t))

"""
Logic:

1. Use two hash maps:
   - map_st for s → t
   - map_ts for t → s

2. Traverse both strings index by index.

3. For each index i:
   - If char_s exists in map_st and map_st[char_s] != char_t → return False
   - Else store mapping map_st[char_s] = char_t

4. Also check reverse:
   - If char_t exists in map_ts and map_ts[char_t] != char_s → return False
   - Else store mapping map_ts[char_t] = char_s

5. If loop completes → return True


Complexity:

Time Complexity  : O(n)  
Space Complexity : O(k)   (k = unique characters)
"""