class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x2 = x
        y = 0
        while x2 != 0:
            y = y * 10 + x2 % 10
            x2 = x2 // 10
        return x == y


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        reverse_x = 0
        while x != 0:
            reverse_x = reverse_x * 10 + x % 10
            x = x // 10
            if reverse_x == x or reverse_x == (x // 10):
                return True
            if reverse_x / x > 1:
                return False


if __name__ == '__main__':
    print(Solution2().isPalindrome(100))