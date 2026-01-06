# Problem :- Given a number n, determine whether it is a prime number or not.
import math
class Solution:
    def isPrime(self,n):
        if n <= 1:
            return False

        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0:
                return False

        return True

s1 = Solution()
print(s1.isPrime(19))


"""
Time Complexity      O(√n)
Space Complexity     O(1)
"""


"""
LOGIC EXPLANATION:

1. A prime number is a number greater than 1
   that has exactly two factors: 1 and itself.

2. If n is less than or equal to 1, it cannot be prime,
   so we immediately return False.

3. To check whether n is prime, we try dividing n by
   numbers starting from 2 up to √n.

4. Why √n?
   - If n = a × b, then at least one of a or b
     must be less than or equal to √n.
   - So if no number up to √n divides n,
     then n has no divisors other than 1 and itself.

5. In the loop:
   - If n % i == 0, then i is a divisor of n,
     which means n is not prime → return False.

6. If the loop finishes without finding any divisor,
   then n is prime → return True.

Time Complexity: O(√n)
Space Complexity: O(1)
"""
