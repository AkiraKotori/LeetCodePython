from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        beg = 0
        end = len(nums) - 1
        while beg <= end:
            mid = (beg + end) // 2
            if nums[mid] < target:
                beg = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return beg


l = list(range(100))
l.pop(10)
Solution().searchInsert(l, 10)
