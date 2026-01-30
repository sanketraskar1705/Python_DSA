# Problem :- Rearrange Array Elements by Sign
"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""
#Brute Solution
class Solution:
    def rearangeArray(self, arr ) :
        pos_arr =[ ]
        neg_arr =[ ]

        for i in range(len(arr)):
            if arr[i] >0 :
                pos_arr.append(arr[i])
            else:
                neg_arr.append(arr[i])

        for i in range(len(pos_arr)) :
            arr[2*i] = pos_arr[i]
            arr[(2*i)+1] = neg_arr[i]

        return arr





s1 = Solution()
arr = [3,-1,4,-4,-3,8]
print(s1.rearangeArray(arr))

"""
Logic Explanation:

1. Create two separate lists:
   - One to store all positive numbers.
   - One to store all negative numbers.
   This helps preserve the original order of elements with the same sign.

2. Traverse the given array:
   - If an element is positive, add it to the positive list.
   - If an element is negative, add it to the negative list.

3. Since the array has an equal number of positive and negative elements,
   both lists will have the same size.

4. Rearrange the original array:
   - Place positive numbers at even indices (0, 2, 4, ...).
   - Place negative numbers at odd indices (1, 3, 5, ...).

5. This ensures:
   - Every consecutive pair has opposite signs.
   - The array starts with a positive number.
   - The relative order of elements with the same sign is preserved.

6. Return the rearranged array as the final result.
"""
