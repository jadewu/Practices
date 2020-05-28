# 两次binary search，分别找到first和last
# 一定要是left<=right，每次二分，移到mid + 1或mid - 1的位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        res = [0, 0]
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        res[1] = right
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = int((left+right)/2)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        res[0] = left
        return res   
