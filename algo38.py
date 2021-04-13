class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            prev_str = self.countAndSay(n - 1)
            curr_str = ''
            last_num = prev_str[0]
            cnt = 1
            for c in prev_str[1:]:
                if c == last_num:
                    cnt += 1
                else:
                    curr_str += str(cnt) + last_num
                    last_num = c
                    cnt = 1
            curr_str += str(cnt) + last_num
            return curr_str


for i in range(1, 30):
    print(Solution().countAndSay(i))