from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        beg_pos = 0
        end_pos = len(nums) - 1
        while beg_pos <= end_pos:
            if nums[beg_pos] == val:
                if nums[end_pos] != val:
                    nums[beg_pos] = nums[end_pos]
                    end_pos -= 1
                else:
                    end_pos -= 1
                    continue
            beg_pos += 1
        return beg_pos

print(Solution().removeElement([4, 5], 5))
