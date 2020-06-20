# 总结一下几种常见的排序算法

# 冒泡排序 Bubble Sort，左右换位，O(n^2)，会超时
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        stop = 0
        while not stop:
            stop = 1
            for i in range(len(nums)-1):
                if nums[i+1] < nums[i]:
                    stop = 0
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            if stop:
                return nums
# 插入排序 Insertion Sort, 新的插入到前面，中间的往后移一位，O(n^2), 会超时
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            tmp = nums[i]
            j = i
            while (j > 0) and (nums[j-1] > tmp):
                nums[j] = nums[j-1]
                j -= 1
            nums[j] = tmp
        return nums

# 合并排序 Merge Sort, 分治法 Divide and Conquer，一分为二直到len=1，合并，recursion，O(nlogn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            
            mid = len(nums)//2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            i, j = 0, 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res
        return mergeSort(nums)

# 堆排序，Heap Sort, 把数存进min heap里，heapify，再拿出，O(logn)/O(h)
# 直接用heapq、min-heap、priorityQueue
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        while nums:
            res.append(heapq.heappop(nums))
        return res
        
# 快排，Quick Sort，也包含分治，选一个pivot，比它小的放左边，比它大的放右边，然后左边右边分别做快排，O(nlogn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            i = low
            pivot = arr[high]
            print(pivot)
            for j in range(low, high):
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
            arr[i], arr[high] = arr[high], arr[i]
            return i
        def quickSort(arr, low, high):
            if low < high:
                pivot = partition(arr, low, high)
                quickSort(arr, low, pivot-1)
                quickSort(arr, pivot+1, high)                
        quickSort(nums, 0, len(nums)-1)
        return nums

# Python自带的Timesort，O(nlogn)，还挺快，综合了合并merge sort和插入insetion sort
# 把整个array分成一些run，分别sort，再插入，合并。。。
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
