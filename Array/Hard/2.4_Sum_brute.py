# Problem :- 4 Sum
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
# Brute Solution
class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []

        my_set = set()

        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        total = nums[i] + nums[j] + nums[k] + nums[l]

                        if total == target:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()              # avoid different order duplicates
                            my_set.add(tuple(temp)) # store unique quadruplet

        result = []
        for quad in my_set:
            result.append(list(quad))

        return result



s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.fourSum(nums,0))

"""
1. First, check if the array has at least 4 elements.
   - If n < 4, no quadruplet is possible, so return empty list.

2. Use four nested loops to generate all possible quadruplets.
   - First loop (i) selects the first element.
   - Second loop (j) selects the second element.
   - Third loop (k) selects the third element.
   - Fourth loop (l) selects the fourth element.
   - Ensure i < j < k < l so all indices are different.

3. Compute the sum of the four selected elements.
   - total = nums[i] + nums[j] + nums[k] + nums[l]
   - If total equals the target, we found a valid quadruplet.

4. Avoid duplicate quadruplets.
   - Sort the quadruplet to make order consistent.
   - Convert it to a tuple and store in a set.
   - Set automatically removes duplicate quadruplets.

5. Convert the set into list of lists.
   - Because the required output format is list of lists.

6. Return the final list of unique quadruplets.

Time Complexity  : O(n⁴)
Space Complexity : O(k)   (k = number of unique quadruplets stored in set)
"""