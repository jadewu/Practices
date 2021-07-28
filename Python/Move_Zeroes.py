# 题目是把0放后面，非0数放前面，并且不能打乱顺序
# 思路是遇到非零的数字和它前面的0交换位置，这样非0数就会挪到前面，0会被换到后面
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
