# Another logic is divided by 10

class Solution:
    def countDigits(self, n: int) -> int:
        if n == 0:
            return 1
        count = 0
        n = abs(n)      # Remove negative sign
        while n > 0:
            n //= 10
            count += 1

        return count

s1=Solution()
print(s1.countDigits(-123))

