from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_total = 0
        max_total = nums[0]
        for n in nums:
            if curr_total + n < n:
                curr_total = n
            else:
                curr_total += n
            if curr_total > max_total:
                max_total = curr_total
        return max_total
