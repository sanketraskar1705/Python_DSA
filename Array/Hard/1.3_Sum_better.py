# Problem :- 3 Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

#Better Solution

class Solution:
    def threeSum(self,nums):

        n = len(nums)
        result = set ( )
        for i in range(n):
            my_set = set()
            for j in range(i+1,n):
                third = -(nums[i]+nums[j])
                if third in my_set:
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])

        return [list(i) for i in result]

s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.threeSum(nums))

"""
1. First, take the length of the array.
   - We will fix one element and try to find the other two elements.

2. Fix the first element using loop (i).
   - For every index i, we try to find two numbers whose sum = -nums[i].

3. Use a set to track visited elements for the second loop.
   - This helps to check in O(1) time whether the required third element exists.

4. For each j > i, compute the required third value.
   - third = -(nums[i] + nums[j])
   - If this value already exists in the set, we found a valid triplet.

5. Avoid duplicate triplets.
   - Sort the triplet so order becomes consistent.
   - Store the triplet as a tuple in a result set.
   - Set automatically removes duplicates.

6. Add nums[j] into the set after checking.
   - So future elements can use it as a possible third value.

7. Convert the result set into list of lists.
   - Because the required output format is list of lists.

8. Return the final list of unique triplets.

Time Complexity  : O(n²)
Space Complexity : O(n)   (for hash set storage)
"""