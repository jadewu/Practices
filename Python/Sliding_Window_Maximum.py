# Deque的做法，O(n)
# 用deque的原因：既需要从左pop，也需要从右pop
# clear的作用：每次把window左边界以外的数从deque里推出popleft()，把比当前位置的数要小的数从deque里拿走pop()
# 第一个for loop：把前k个数在deque里安排好，找出最大值
# 第二个for loop：从第k+1个开始，一个一个挪动往右，做clear操作
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k == 0:
            return []
        if k == 1:
            return nums
        def clear(q, i):
            if q and q[0] == i-k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
        deq = collections.deque()
        idx = 0
        for i in range(1, k):
            clear(deq, i)
            deq.append(i)
            if nums[i] > nums[idx]:
                idx = i
        # print(deq)
        res = [nums[idx]]
        for i in range(k, n):
            # print(deq, i, res)
            clear(deq, i)
            deq.append(i)
            res.append(nums[deq[0]])
        return res
            
