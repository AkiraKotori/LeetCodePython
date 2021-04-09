from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if strs:
            strs.sort()
            for c1, c2 in zip(strs[0], strs[-1]):
                if c1 == c2:
                    prefix += c1
                else:
                    return prefix
        return prefix