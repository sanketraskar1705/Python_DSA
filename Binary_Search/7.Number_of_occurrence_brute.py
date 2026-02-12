#Problem :- Count occurrences of a number in a sorted array with duplicates
#Brute Solution
class Solution:
    def noOfoccurrence(self,nums,target):
        n = len(nums)
        count = 0
        for i in range(0,n):
            if nums[i] == target:
                count += 1

        return count

s1 = Solution()
nums = [1,1,2,2,2,2,3,4,6,6,7,8,9]
target = 2
print(s1.noOfoccurrence(nums,target))

"""
1. Goal:
   Count how many times the target appears in the array.

2. Initialize:
   count = 0 (to store total occurrences)

3. Traverse the array from index 0 to n-1.

4. For each element:
   - If nums[i] == target:
       → increase count by 1

5. After completing the loop:
   - count stores total occurrences of target
   - If target does not appear → count remains 0

6. Return count

------------------------------------------------------------

Time Complexity  : O(n)
Space Complexity : O(1)
"""