# Problem :- Print all Divisors or Factors of a number

class Solution:
    def solve(self,n):
        result = []
        for i in range(1,n//2+1):
            if(n % i == 0):
                result.append(i)

        result.append(n)

        return result

s1=Solution()
print(s1.solve(20))

"""
LOGIC EXPLANATION:

1. Any number greater than 1 cannot have a divisor
   greater than n/2 except the number itself.

2. Therefore, instead of checking from 1 to n,
   we check from 1 to n//2 to find all possible divisors.

3. For each number i in this range:
   - If n % i == 0, then i is a divisor of n.
   - We add i to the result list.

4. After the loop, we explicitly add n because
   every number is divisible by itself.

5. This approach reduces unnecessary checks compared
   to looping till n, but it still checks many values.

Time Complexity: O(n)
Space Complexity: O(n)
"""
