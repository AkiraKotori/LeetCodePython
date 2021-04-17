class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            size = len(a)
            long_str = b
        else:
            size = len(b)
            long_str = a
        pos = 0
        ans = ''
        carry = 0
        while pos != size:
            if a[len(a) - pos - 1] == '1' and b[len(b) - pos - 1] == '1':
                if carry:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                carry = 1
            elif a[len(a) - pos - 1] == '0' and b[len(b) - pos - 1] == '0':
                if carry:
                    ans = '1' + ans
                else:
                    ans = '0' + ans
                carry = 0
            else:
                if carry:
                    ans = '0' + ans
                    carry = 1
                else:
                    ans = '1' + ans
            pos += 1
        while pos != len(long_str):
            if carry == 0:
                ans = long_str[len(long_str) - pos - 1] + ans
            else:
                if long_str[len(long_str) - pos - 1] == '1':
                    ans = '0' + ans
                else:
                    ans = '1' + ans
                    carry = 0
            pos += 1
        if carry:
            ans = '1' + ans
        return ans


if __name__ == '__main__':
    assert Solution().addBinary('11', '1') == '100'
