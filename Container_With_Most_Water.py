# Two pointers, 左右分别开始，缩进较短的那一边可能可以得到更大结果，因为计算水量的长度是由较短的一边决定的
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1
        while left < right:
            res = max(res, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
