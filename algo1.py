from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n = nums[i]
            other_nums = nums[i + 1:]
            if (target - n) in other_nums:
                j = nums.index(target - n, i + 1)
                return [i, j]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for index, n in enumerate(nums):
            if target - n in s:
                return [index, s[target - n]]
            s[n] = index


if __name__ == '__main__':
    print(Solution().twoSum([0, 4, 3, 0], 0))
