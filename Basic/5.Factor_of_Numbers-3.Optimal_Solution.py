# Problem :- Print all Divisors or Factors of a number
from math import sqrt

class solution:
    def solve(self,n):
        result = []

        for i in range(1,int(sqrt(n)+1)):
            if n % i == 0:
                if n//i != i :
                    result.append(i)


        result.append(n)
        return result

s1=solution()
print(s1.solve(15))

"""
LOGIC EXPLANATION:

1. Divisors of a number always occur in pairs.
   Example: For n = 15
   (1, 15) and (3, 5)

2. In every divisor pair:
   - One number is smaller than or equal to √n
   - The other number is greater than or equal to √n

3. So instead of checking all numbers from 1 to n,
   we only iterate from 1 to √n to reduce time complexity.

4. For each number i in the range:
   - If n % i == 0, then i is a divisor.
   - The paired divisor is n // i.

5. The condition (n // i != i) avoids adding the same
   divisor twice in case of a perfect square.

6. Finally, n is added explicitly since every number
   is divisible by itself.

Time Complexity: O(√n)
Space Complexity: O(√n)
"""
