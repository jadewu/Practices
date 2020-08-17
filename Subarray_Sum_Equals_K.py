# 用dict存储各个sum的subarray有几个
# 比如nums = [1,3,2,2,2], k = 4
# 遍历的时候cur的变化：1, 4, 6, 8, 10
# 在第一个数的时候：cur=1, cur-k=-3, d[-3] = 0, d[1] = 1, count = 0
# 在第二个数的时候：cur=4, cur-k=0, d[0] = 1 (前面有从头开始和为0的subarray), d[4] = 1, count = 1
# 在第三个数的时候：cur=6, cur-k=2, d[2] = 0, d[6] = 1, count = 1
# 在第四个数的时候：cur=8, cur-k=4, d[4] = 1 (前面有从头开始和为4的subarray), d[8] = 1, count = 2
# 在第五个数的时候：cur=10, cur-k=6, d[6] = 1 (前面有从头开始的和为6的subarray), d[10] = 1, count = 3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        count = 0
        d[0] = 1
        cur = 0
        for n in nums:
            cur += n
            count += d[cur-k]
            d[cur] += 1
            # print(cur, count, d)
        return count
