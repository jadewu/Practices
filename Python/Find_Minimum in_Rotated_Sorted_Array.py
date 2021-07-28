# The list is in ascending order but moving left part to the front like (4,5,1,2,3)
# Binary search is efficient in finding an element in sorted list
# 只需要比较mid和r的大小，因为发生旋转，一定是从右边挪到左边，所以旋转后的最右一定比最左小
# 如果旋转后的最右比mid小，那么最小值一定在mid右边；相反，最小值在mid左边
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        # nums.sort()
        return nums[l]
