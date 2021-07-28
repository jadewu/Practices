# stack的做法，如果比stack[-1]大就逐个往前pop，同时计算面积
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        i = 0
        while (i < len(height)):
            while stack and (height[i] > height[stack[-1]]):
                low = height[stack[-1]]
                stack.pop()
                if not stack:
                    break
                w = i - stack[-1] -1
                high = min(height[i], height[stack[-1]])
                h = high - low
                res += h*w
            stack.append(i)
            i += 1
        return res

# 左右两个指针的做法，分别碰到比max height小的时候，就计算面积
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0
        left_max, right_max = 0, 0
        while (left<right):
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    res += (left_max - height[left])
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
