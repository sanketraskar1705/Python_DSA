# Problem :- Print all Divisors or Factors of a number

class Solution:
    def solve(self, n):
        result = [ ]
        for i in range(1,n+1):
            if n % i == 0 :
                result.append(i)

        return result

s1=Solution()
print(s1.solve(15))

"""
LOGIC EXPLANATION:

1. The goal is to find all divisors (factors) of a number n.

2. A divisor is a number that divides n completely
   (i.e., remainder is 0).

3. We iterate from 1 to n because:
   - 1 is always a divisor of any number.
   - n is always divisible by itself.

4. For each number i in this range:
   - If n % i == 0, then i is a divisor of n.
   - We add i to the result list.

5. This approach checks every possible number,
   so it guarantees all divisors are found.

Time Complexity: O(n)
Space Complexity: O(n)
"""
