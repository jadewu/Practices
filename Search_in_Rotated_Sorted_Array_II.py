# Binary Search，在search rotated sorted array的基础上，加上等于的时候一个个遍历，O(logn)~O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == target:
                return True
            if nums[r] == target:
                return True
            if (r > len(nums)-1) or (l < 0):
                return False
            if nums[mid] > nums[l]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                r = r - 1
                
        return False
