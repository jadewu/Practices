# 一次二分法，分情况讨论
# 如果中间值比左边大，且target在左边和中间值之间，则target一定在一段递增数列里，只需要把右边向左移就行
# 如果中间值比左边大，且target比左边小或者target比中间值大，左边向右移
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[i]:
                if target >= nums[i] and target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if target <= nums[j] and target > nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1

# 三次二分法，先找到rotate的起点，结合LC153，得到两段单调递增的数列
# 然后通过常规二分法，判断target是否在这两段数列里
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i < j:
            mid = (i+j)//2
            if nums[mid] <= nums[j]:
                j = mid
            else:
                i = mid + 1
        def bs(arr, tar):
            if not arr:
                return -1
            i, j = 0, len(arr)-1
            while i < j:
                mid = (i+j)//2
                if tar == arr[mid]:
                    return mid
                elif tar < arr[mid]:
                    j = mid
                else:
                    i = mid + 1
            if arr[i] == tar:
                return i
            return -1
        res1 = bs(nums[:i], target)
        print(nums[:i], res1)
        res2 = bs(nums[i:], target)
        print(nums[i:], res2)
        if res1 != -1:
            return res1
        elif res2 != -1:
            return res2 + i
        return -1

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

