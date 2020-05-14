# If using for loops to calculate longest continuous width below a given heights,
# this will cost O(n^2) time, and lead to time out.
# Use stack to simplify to O(n)

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)

            stack.append(i)
        heights.pop()
        return res
