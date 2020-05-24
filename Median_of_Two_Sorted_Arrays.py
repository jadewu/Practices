# 高频考题，二分法递归，详细解析看leetcode答案

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
