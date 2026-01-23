# Problem :- Remove duplicate from sorted array
# Brute Solution


class Solution:
    def removeDuplicates(self, arr):
        n=len(arr)
        freq_map={ }

        for i in range(n):
            freq_map[arr[i]]=0

        j=0
        for k  in freq_map:
            arr[j]=k
            j+=1

        return j

s1 = Solution()
arr = [1,1,1,2,3,3,4,4,4,4,5]
length =s1.removeDuplicates(arr)
print(length)
print(arr[:length])

# Time complexity  :- o(2n)
# Space Complexity :- o(n)

"""
1. Create a hash map to store unique elements from the array.
2. Traverse the array and insert each element as a key in the hash map.
3. Since keys in a hash map are unique, duplicates are automatically removed.
4. Traverse the hash map and place each unique key back into the array.
5. Count how many unique elements are inserted and return that count.
6. The first part of the array up to the returned length contains unique elements.
"""


