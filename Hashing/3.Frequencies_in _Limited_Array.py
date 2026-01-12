# Problem :-You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent.
# Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).
# example:- Input: arr[] = [2, 3, 2, 3, 5]
# Output: [0, 2, 2, 0, 1]
# Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.


class Solution:
    def freqCount(self,arr):
        result = [0] * len(arr)

        for num in arr:
            result[num-1] += 1

        return result

s1=Solution()
print(s1.freqCount([2,4,0,7,2,6,6,1,8]))


























"""
Logic:
1. Find the size of the array (n).
2. Create a result array of size n and initialize all values with 0.
3. Each index of the result array represents numbers from 1 to n.
4. Traverse the given array element by element.
5. For each number, convert it to index by subtracting 1 (num - 1).
6. Increment the value at that index to count the frequency.
7. After traversing all elements, return the result array.
"""
