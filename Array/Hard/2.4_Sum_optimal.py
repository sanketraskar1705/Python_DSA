# Problem :- 4 Sum
"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
"""
# Optimal Solution
class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i  > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k > l and nums[l] == nums[l+1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return ans

s1 = Solution()
nums = [-1,0,1,2,-1,-4]
print(s1.fourSum(nums,0))

"""
1. First, sort the array.
   - Sorting helps in using the two-pointer technique.
   - It also makes it easy to skip duplicate elements.

2. Fix the first element using loop (i).
   - If current element is same as previous, skip it to avoid duplicate quadruplets.

3. Fix the second element using loop (j).
   - If current element is same as previous (for this loop), skip it to avoid duplicates.

4. Use two pointers to find the remaining two elements.
   - k = j + 1  → start pointer
   - l = n - 1  → end pointer
   - Now we search for two numbers such that:
     nums[i] + nums[j] + nums[k] + nums[l] == target

5. Calculate the total sum of four elements.
   - If total == target → valid quadruplet found → store it.
   - Move both pointers inward (k += 1, l -= 1).

6. Skip duplicate values for k and l.
   - Move k forward while nums[k] == nums[k-1].
   - Move l backward while nums[l] == nums[l+1].
   - This ensures unique quadruplets only.

7. If total < target → increase sum.
   - Move k forward (k += 1).

8. If total > target → decrease sum.
   - Move l backward (l -= 1).

9. Continue until k < l.
   - This completes search for current i and j.

10. Return the list of unique quadruplets.

Time Complexity  : O(n³)
Space Complexity : O(1) auxiliary (excluding output list)
"""