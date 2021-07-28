# 二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        if not nums:
            return 0
        while i <= j:
            mid = (i + j)//2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        return i

# 直接遍历的解法，O(n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        return len(nums)
