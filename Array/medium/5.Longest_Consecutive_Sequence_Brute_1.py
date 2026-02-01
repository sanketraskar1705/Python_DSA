# Problem :- Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Brute Solution

class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)
        max_count = 0
        for i in range(n):
            num = nums[i]
            count = 1

            while num+1 in nums:
                count += 1
                num = num+1

            max_count = max(max_count, count)

        return max_count

s1 = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(s1.longestConsecutive(nums))

"""
        LOGIC:
        1. Traverse each element of the array.
        2. Take the current element as the starting number of a sequence.
        3. Initialize count as 1 because the current number itself forms a sequence.
        4. Check whether the next consecutive number (num + 1) exists in the array.
        5. If it exists, move to the next number and increase the count.
        6. Keep extending the sequence until the next number is not found.
        7. After finishing one sequence, update the maximum length found so far.
        8. Repeat this process for all elements and return the maximum count.
"""