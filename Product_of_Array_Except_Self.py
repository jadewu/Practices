# Two pass, O(n) time, O(1) space
# 第一遍从左向右乘，每一项的结果都是这一项左边的所有数的乘积
# 第二遍从右向左乘，每一项的结果再乘上这一项右边的所有数的乘积
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i-1] * res[i-1]
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * right
            right *= nums[i]
        return res

# One pass, 左右一起操作
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            res[i] *= left
            res[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        return res
