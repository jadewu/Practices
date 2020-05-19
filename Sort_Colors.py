# Can not use sort()
# One pass in place without swap，
# i和j是pivot用来记下一个0/1应该写在哪
# 遍历的时候先把值改成2，如果原来的值是1，就把j标记的地方改成1，i和j都+1
# 如果原来的值是0，就把i标记的地方改成0，只有i+1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            t = nums[k]
            nums[k] = 2
            if t < 2:
                nums[j] = 1
                j += 1
            if t == 0:
                nums[i] = 0
                i += 1
            print(nums)

# Use swap
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        k = len(nums)-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
