class Solution:
    def maxArea(self, heights: List[int]) -> int:
        count = 0
        end = len(heights) - 1
        start = 0
        while start < end:
            length = end - start
            mini = min(heights[start], heights[end])
            fill = length * mini
            if count < fill:
                count = fill
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1
        return count
