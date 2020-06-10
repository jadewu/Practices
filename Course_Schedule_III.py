# Greedy, 用heapq来实现priorityQueue
# 将原数列按结束如期从小到大排列，依次把时长放入heap
# 如果得到的完成日期超过当前限定日期，就把耗时最长的取出
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq = []
        start = 0
        for t, d in sorted(courses, key=lambda x: x[1]):
            # print(t, d)
            # print(pq)
            start += t
            heapq.heappush(pq, -t)
            while start > d:
                start += heapq.heappop(pq)
                # print(start, len(pq))
            
        return len(pq)
