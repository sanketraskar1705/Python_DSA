# Problem :- 4 Sum
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
# Better Solution

class Solution:
    def fourSum(self,nums,target):
        n = len(nums)
        my_set = set()
        for i in range(n):
            for j in range(i+1,n):
                hash_set = set()
                for k in range(j+1,n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hash_set:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        my_set.add(tuple(temp))
                    hash_set.add(nums[k])

        result = []
        for ans in my_set:
            result.append(list(ans))

        return result

s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.fourSum(nums,0))

"""
1. First, take the length of the array.
   - We will fix two elements and try to find the remaining two elements.

2. Use two nested loops to fix the first two elements.
   - First loop (i) selects the first element.
   - Second loop (j) selects the second element.
   - Now we need two more elements whose sum = target - (nums[i] + nums[j]).

3. Use a hash set to track visited elements for the third loop.
   - This allows checking in O(1) time whether the required fourth element exists.

4. For each k > j, compute the required fourth value.
   - fourth = target - (nums[i] + nums[j] + nums[k])
   - If this value already exists in the hash set, we found a valid quadruplet.

5. Avoid duplicate quadruplets.
   - Sort the quadruplet so order becomes consistent.
   - Convert it into a tuple and store in a set.
   - Set automatically removes duplicate quadruplets.

6. Add nums[k] into the hash set after checking.
   - So future elements can use it as a possible fourth value.

7. Convert the result set into list of lists.
   - Because the required output format is list of lists.

8. Return the final list of unique quadruplets.

Time Complexity  : O(n³)
Space Complexity : O(n)   (for hash set storage)
"""