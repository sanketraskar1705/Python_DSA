# Problem :- Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        my_set = set()
        n = len(nums)
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num -1 not in my_set:
                x = num
                count = 1
                while x+1 in my_set:
                    count += 1
                    x += 1
                longest = max(longest,count)

        return longest

s1 = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(s1.longestConsecutive(nums))

"""
        LOGIC:
        1. Create a set from the array to remove duplicates and allow O(1) lookup.
        2. Iterate through each number in the set.
        3. Start counting a sequence only if the current number is the
           beginning of a sequence (i.e., number - 1 is not present in the set).
        4. Once a starting number is found, keep checking for the next
           consecutive numbers (x + 1, x + 2, ...) in the set.
        5. Increase the count for each consecutive number found.
        6. Update the longest sequence length after finishing each sequence.
        7. After checking all possible sequences, return the longest length.
"""