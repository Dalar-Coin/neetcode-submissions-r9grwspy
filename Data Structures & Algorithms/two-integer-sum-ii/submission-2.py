class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers)):
            temp = numbers[left] + numbers[right]

            if temp > target:
                right -= 1
            elif temp < target:
                left += 1
            else:
                return [left+1, right+1]