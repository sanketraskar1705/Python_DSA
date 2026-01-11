# Problem :- Store the frequency of numbers in a list using a dictionary.


class Solution:
    def frequencyStore(self,arr):
        freq_map = { }
        for i in range(0,len(arr)):
            if arr[i] not in freq_map:
                freq_map[arr[i]] = 1
            else:
                freq_map[arr[i]] += 1

        return freq_map

s1 = Solution()
print(s1.frequencyStore([1,2,3,4,5,3,6,4,7,3,6,2,1,5,7,8,97]))

