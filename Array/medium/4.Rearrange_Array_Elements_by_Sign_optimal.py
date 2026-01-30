# Problem :- Rearrange Array Elements by Sign
"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""
# Optimal Solution
class Solution:
    def rearrangeArray(self, nums):
        n = len(nums)
        res = [0]*n
        pos_ind, neg_ind = 0,1
        for i in range(n):
            if nums[i] >= 0:
                res[pos_ind] = nums[i]
                pos_ind += 2
            else:
                res[neg_ind] = nums[i]
                neg_ind += 2
        return res

s1 = Solution()
nums = [8,-1,-4,3,-2,1]
print(s1.rearrangeArray(nums))

"""
Logic Explanation (Optimal Solution):

1. Create a result array of the same size as the input array,
   initialized with zeros. This array will store the final rearranged result.

2. Use two pointers:
   - pos_ind starting at index 0 for placing positive numbers.
   - neg_ind starting at index 1 for placing negative numbers.
   This ensures the array starts with a positive number and signs alternate.

3. Traverse the input array once:
   - If the current element is positive, place it at pos_ind in the result array
     and move pos_ind by 2 to the next even index.
   - If the current element is negative, place it at neg_ind in the result array
     and move neg_ind by 2 to the next odd index.

4. Since the array contains an equal number of positive and negative elements,
   both pointers will always remain within the bounds of the result array.

5. This approach maintains:
   - Alternating positive and negative signs.
   - The original relative order of elements with the same sign.
   - An optimal time complexity of O(n) and space complexity of O(n).

6. Return the result array as the final rearranged array.
"""
