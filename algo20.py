SYMBOL = {')': '(', ']': '[', '}': '{'}


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        for c in s:
            if c not in SYMBOL:
                stack.append(c)
            else:
                if not stack or stack.pop() != SYMBOL[c]:
                    return False
        if stack:
            return False
        return True
