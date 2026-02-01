# Problem :- Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # start only if it's the beginning of a sequence
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest


s1 = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(s1.longestConsecutive(nums))


"""
        LOGIC:
        1. Convert the list into a set so that lookup (search) takes O(1) time.
        2. Iterate through each number in the set.
        3. Treat a number as the start of a sequence ONLY if (number - 1) is not present.
           This avoids counting the same sequence multiple times.
        4. Once a start is found, keep checking for the next consecutive numbers
           (number + 1, number + 2, ...) in the set.
        5. Count the length of this consecutive sequence.
        6. Update the maximum length found so far.
        7. Return the maximum consecutive sequence length.
"""
