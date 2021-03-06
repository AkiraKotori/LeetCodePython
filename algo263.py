class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while n != 1:
            if not n % 2:
                n = n // 2
            elif not n % 3:
                n = n // 3
            elif not n % 5:
                n = n // 5
            else:
                return False
        return True