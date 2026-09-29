class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in checker:
                return [checker[diff], i]
            checker[n] = i
                