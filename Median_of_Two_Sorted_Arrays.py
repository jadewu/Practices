# 最容易想的解法，一个一个比对，用prev记录上一次的数字
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n%2:
                return nums2[n//2]
            else:
                return (nums2[n//2]+nums2[n//2-1])/2
        if n == 0:
            if m%2:
                return nums1[m//2]
            else:
                return (nums1[m//2]+nums1[m//2-1])/2
        ct = (m+n)//2
        i, j = 0, 0
        cur, prev = 0, 0
        while ct >= 0:
            if i == m:
                if ct > 0:
                    cur = nums2[j]
                break
            if j == n:
                if ct > 0:
                    cur = nums1[i]
                break
            prev = cur
            if nums1[i] <= nums2[j]:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
            ct -= 1
        if ct >= 0:
            prev = cur
            if i < m:
                cur = nums1[i+ct]
                if ct > 0:
                    prev = nums1[i+ct-1]
            else:
                cur = nums2[j+ct]
                if ct > 0:
                    prev = nums2[j+ct-1]
        if (m+n)%2:
            res = cur
        else:
            res = (prev + cur)/2
        print(prev, cur)
        return res

# 两个heap的做法，一个最大堆一个最小堆，分别存一半，每次insert的时候比较树和最大堆的最小值的大小
# 最后需要平衡两个堆的长度，调整到相等或者差1
import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            if len(nums2)%2:
                return nums2[len(nums2)//2]
            else:
                return (nums2[len(nums2)//2]+nums2[len(nums2)//2-1])/2
        max_heap = [nums1[0]]
        min_heap = []
        nums = nums1[1:] + nums2
        for num in nums:
            sm = heapq.heappop(max_heap)
            if num < sm:
                heapq.heappush(min_heap, -num)
                heapq.heappush(max_heap, sm)
            else:
                heapq.heappush(max_heap, num)
                heapq.heappush(min_heap, -sm)
        # print(max_heap, min_heap)
        if len(nums)%2:
            while len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(max_heap) < len(min_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            res = (heapq.heappop(max_heap)-heapq.heappop(min_heap))/2
        else:
            while len(max_heap) > len(min_heap)-1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(max_heap) < len(min_heap)-1:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            res = -heapq.heappop(min_heap)
        return res

# 时间最优解，二分法递归，log(min(m, n))复杂度，详细解析看leetcode答案
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half = 0, m, int((m+n+1)/2)
        
        while imin <= imax:
            i = int((imin + imax)/2)
            j = half - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                    
                if (m + n) % 2:
                    return max_of_left
                    
                if i == m: 
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else: 
                    min_of_right = min(A[i], B[j])
                print(max_of_left)
                print(min_of_right)
                return (max_of_left + min_of_right)/2
