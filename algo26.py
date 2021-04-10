from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        insert_pos = 0
        value_pos = 1
        while value_pos != len(nums):
            if nums[insert_pos] == nums[value_pos]:
                value_pos += 1
            else:
                insert_pos += 1
                nums[insert_pos] = nums[value_pos]
                value_pos += 1
        return insert_pos + 1


if __name__ == '__main__':
    nums = [1, 1, 2, 3, 3, 4, 5]
    print(Solution().removeDuplicates(nums))
    print(nums)