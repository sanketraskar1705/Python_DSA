# Problem :- 3 Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Brute Solution

class Solution:
    def threeSum(self,nums):
        n = len(nums)

        my_set = set()
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        temp = [nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))

        return [list(ans) for ans in my_set]


s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.threeSum(nums))

"""
1. First, take the length of the array.
   - We need three different indices i, j, k such that i < j < k.

2. Use three nested loops to generate all possible triplets.
   - Outer loop selects first element (i).
   - Middle loop selects second element (j).
   - Inner loop selects third element (k).

3. Check if the sum of the triplet is equal to zero.
   - If nums[i] + nums[j] + nums[k] == 0, then it is a valid triplet.

4. Avoid duplicate triplets.
   - Sort the triplet so that order becomes consistent.
   - Convert the triplet into a tuple and store it in a set.
   - Set automatically removes duplicate triplets.

5. Convert the set back into list of lists.
   - Because the required output format is list of lists.

6. Return the final list of unique triplets.

Time Complexity  : O(n³)
Space Complexity : O(k)   (k = number of unique triplets stored in set)
"""