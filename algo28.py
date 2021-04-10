class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or haystack == needle:
            return 0
        pos = 0
        while pos <= len(haystack) - len(needle):
            if haystack[pos] == needle[0]:
                i = 1
                while i != len(needle):
                    if haystack[pos + i] != needle[i]:
                        break
                    i += 1
                if i == len(needle):
                    return pos
            pos += 1
        return -1


Solution().strStr("abc", "c")
