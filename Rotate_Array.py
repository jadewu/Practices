# 先整个倒一遍，再把前面k个倒回去，最后把剩下的倒回去
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(l, start, end):
            while start < end:
                l[start], l[end] = l[end], l[start]
                start += 1
                end -= 1
            return l
        n = len(nums)
        k = k % n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
