# Problem :- Given a number n, determine whether it is a prime number or not.
# Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

class Solution:
    def isPrime(self,n):
        result = [ ]

        for i in range(1,n+1):
            if n % i == 0:
                result.append(i)

        return len(result) == 2

s1 = Solution()
print(s1.isPrime(10))
print(s1.isPrime(7))

"""
Time complexity     	Space complexity
    O(n)	                  O(n)

"""