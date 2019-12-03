import math
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev = 0
        while( x > 0 ):
            dig = x % 10
            rev = rev * 10 + dig
            x = x // 10
        if(rev > 0 and math.ceil(math.log(rev, 2)) > 31):
            return 0
        return rev * sign

solution = Solution()

print(solution.reverse(0))

