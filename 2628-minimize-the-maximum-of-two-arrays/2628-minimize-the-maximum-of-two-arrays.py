class Solution:
    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def can(x):
            cnt1 = x - x // divisor1
            cnt2 = x - x // divisor2
            lcm = divisor1 * divisor2 // self.gcd(divisor1, divisor2)
            both = x - x // divisor1 - x // divisor2 + x // lcm
            only1 = cnt1 - both
            only2 = cnt2 - both
            need1 = max(0, uniqueCnt1 - only1)
            need2 = max(0, uniqueCnt2 - only2)
            return need1 + need2 <= both

        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
