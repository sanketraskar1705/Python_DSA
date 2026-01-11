# Problem :- Store the frequency of numbers in a list using a dictionary.

class Solution:
    def FrequencyMap(self, arr):
        hash_map = dict()

        for i in range(len(arr)):
            hash_map[arr[i]] = hash_map.get(arr[i],0)+1

        return hash_map

s1 = Solution()
print(s1.FrequencyMap([1,2,32,32,1,4,5,8,8,4,5,9,7,2,1,4]))


"""
Logic:
1. Create an empty dictionary to store frequency of elements.
2. Traverse the array element by element.
3. If the element exists in the dictionary, increment its count by 1.
4. If the element does not exist, add it to the dictionary with count 1.
5. After processing all elements, return the dictionary containing frequencies.
"""
