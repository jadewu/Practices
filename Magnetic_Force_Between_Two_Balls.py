# 二分法
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        print(position)
        n = len(position)
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            count = 1
            cur = position[0]
            for i in range(1, n):
                if position[i] - cur >= mid:
                    count += 1
                    cur = position[i]
            if count >= m:
                l = mid
            else:
                r = mid - 1
        return l
