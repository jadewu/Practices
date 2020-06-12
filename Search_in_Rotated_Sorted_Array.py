# 分情况讨论，想了好久，非常难受
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if not nums:
            return -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

