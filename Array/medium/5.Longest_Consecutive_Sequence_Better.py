# Problem :- Longest Consecutive Sequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Better Solution

class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        count = 0
        last_smaller = float("-inf")
        longest = 0

        for i in range(0, len(nums)):
            num = nums[i]

            if num - 1 == last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num

            longest = max(longest, count)

        return longest

s1 = Solution()
nums = [100,4,200,1,3,2]
print(s1.longestConsecutive(nums))


"""
        LOGIC:
        1. First, sort the array so consecutive numbers come next to each other.
        2. Initialize:
           - count to track the current consecutive sequence length
           - last_smaller to store the previous number in the sequence
           - longest to store the maximum sequence length found
        3. Traverse the sorted array one element at a time.
        4. If the current number is exactly 1 greater than the previous number,
           it means the consecutive sequence continues, so increment count.
        5. If the current number is not equal to the previous number
           (handles duplicate values), start a new sequence by resetting count to 1.
        6. Update last_smaller with the current number after every iteration.
        7. Keep updating the longest sequence length.
        8. After completing the loop, return the longest consecutive sequence length.
"""
