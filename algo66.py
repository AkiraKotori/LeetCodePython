from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        while pos != 0:
            if digits[pos] == 9:
                digits[pos] = 0
                pos -= 1
            else:
                break
        if digits[pos] == 9:
            digits[pos] = 0
            return [1] + digits
        else:
            digits[pos] += 1
            return digits
