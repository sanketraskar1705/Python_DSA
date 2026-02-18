# Problem:- Largest odd number in a string
class Solution:
    def largestOddNumber(self,nums):
        n = len(nums)
        for i in range(n-1,-1,-1):
            if int(nums[i]) % 2 == 1:
                return nums[:i+1]
        return ""

s1 = Solution()
nums = "57234"
print(s1.largestOddNumber(nums))

"""
Logic:

1. We need to find the largest odd number from the given numeric string.

2. A number is odd if its last digit is odd (1, 3, 5, 7, 9).

3. To get the largest odd substring, start checking digits from right to left.

4. For each digit (from end to start):
   - Convert the character to integer.
   - Check if it is odd using (digit % 2 == 1).

5. If an odd digit is found at index i:
   - Return substring from index 0 to i (nums[:i+1]).
   - This substring forms the largest odd number.

6. If no odd digit is found after scanning entire string:
   - Return empty string "" because no odd number exists.


Complexity:

Time Complexity  : O(n)   → We scan the string once from right to left.  
Space Complexity : O(1)   → No extra space is used (constant memory).
"""