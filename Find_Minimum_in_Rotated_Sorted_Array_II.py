# 多加一个mid == r的情况，右边向中间靠拢，最坏O(n)，最好O(logn)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                r = mid
        # nums.sort()
        return nums[l]
