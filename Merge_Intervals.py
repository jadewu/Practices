# 先sort再比较每个interval的右边界，一个个合并，O(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        intervals.sort()
        # print(intervals)
        res = [intervals[0]]
        maxi = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= maxi:
                if intervals[i][1] > maxi:
                    res[-1][1] = intervals[i][1]
                    maxi = intervals[i][1]
            else:
                res.append(intervals[i])
                maxi = intervals[i][1]
                
            # print(maxi)
        return res
