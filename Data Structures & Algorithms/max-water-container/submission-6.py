class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            minBar = min(heights[l], heights[r])
            diffVar = r - l
            currMax = minBar * diffVar
            if currMax > maxA:
                maxA = currMax
            if minBar == heights[l]:
                l += 1
            elif minBar == heights[r]:
                r -= 1
        
        return maxA