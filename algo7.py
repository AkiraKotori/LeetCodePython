MAX = 2**31 - 1
MIN = -2 * 31


class Solution:
    def reverse(self, x: int) -> int:
        out_n = 0
        if x < 0:
            flag = -1
            x = -x
        else:
            flag = 1
        while x != 0:
            r = x % 10
            x = x // 10
            out_n = out_n * 10 + r
        if out_n < MIN or out_n > MAX:
            return 0
        return out_n * flag


if __name__ == '__main__':
    print(Solution().reverse(-123))