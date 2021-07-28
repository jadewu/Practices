# Min Heap是最快的
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap O(nlogk)
        h = nums[:k]
        heapq.heapify(h)
        for i in range(k, len(nums)):
            top = heapq.heappop(h)
            if nums[i] > top:
                heapq.heappush(h, nums[i])
            else:
                heapq.heappush(h, top)
        return heapq.heappop(h)
        Partition O(n)
        
        # QuickSelect, O(n)~O(n^2)
        return self.quickSelect(nums, 0, len(nums)-1, k)

    def quickSelect(self, nums, start, n, k): # quick select
        pos = self.partition(nums, start, n)
        if pos == k-1:
            return nums[pos]
        elif pos >= k:
            return self.quickSelect(nums, start, pos - 1, k)
        return self.quickSelect(nums, pos + 1, n, k)

    def partition(self, nums, left, right):
        pivot = nums[right] # pick the last one as pivot
        i = left
        for j in range(left, right): # left to right -1
            if nums[j] > pivot: # the larger elements are in left side
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i
        
        # Sort(), O(nlogn)
        nums.sort()
        return nums[len(nums)-k]
        
        # Bubble sort, O(nk)
        l = len(nums)
        for i in range(k):
            for j in range(l-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        print(nums)
        return nums[l-k]
                
            
