# Problem :- Two sum
# Optimal solution

class Solution:
    def twoSum(self,arr,target):
        n = len(arr)
        hash_map = { }
        for i in range(n):
            remaining = target - arr[i]
            if remaining in hash_map:
                return [hash_map[remaining],i]
            else:
                hash_map[arr[i]] = i


s1 = Solution()
arr = [2,7,11,15]
target = 9
print(s1.twoSum(arr,target))


"""
        Logic:
        1. Create an empty hash_map (dictionary) to store numbers and their indices.
        2. Traverse the array one element at a time.
        3. For each element arr[i], calculate the remaining value needed:
           remaining = target - arr[i]
        4. Check if this remaining value already exists in hash_map:
           - If yes, it means we have found two numbers whose sum is equal to target.
             Return the index of the remaining value (from hash_map)
             and the current index i.
        5. If remaining is not found, store the current element arr[i]
           along with its index i in the hash_map.
        6. This approach works in O(n) time because dictionary lookups are O(1).
"""