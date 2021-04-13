class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for c in s[::-1]:
            if c == ' ' and not cnt:
                continue
            elif c == ' ':
                break
            cnt += 1
        return cnt