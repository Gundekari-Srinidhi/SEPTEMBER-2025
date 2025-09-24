class Solution:
    def findNthDigit(self, n: int) -> int:
        def total_digits(x):
            digits = 0
            length = 1
            start = 1
            while start <= x:
                end = min(x, start * 10 - 1)
                digits += (end - start + 1) * length
                start *= 10
                length += 1
            return digits
        left, right = 1, 10**18
        while left < right:
            mid = (left + right) // 2
            if total_digits(mid) >= n:
                right = mid
            else:
                left = mid + 1
        x = left 
        prev = total_digits(x - 1)  
        idx = n - prev              
        return int(str(x)[idx - 1])
