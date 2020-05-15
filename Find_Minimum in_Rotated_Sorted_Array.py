# The list is in ascending order but moving left part to the front like (4,5,1,2,3)
# Binary search is efficient in finding an element in sorted list
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        
        # binary search
        while left < right:
            mid = (left+right)//2
            print(mid)
            if nums[mid] < nums[right]:
                # minimum is between left and mid
                right -= 1
            else:
                # minimum is between mid and right
                left += 1
        return nums[left]
