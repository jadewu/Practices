# 每次当刚好满足包含所有元素的所有出现的substrings时，就截取，Greedy
# 这样能让剩下的部分更长，也会产生更多的slices
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {}
        for i, c in enumerate(S):
            last[c] = i
        start = end = 0
        res = []
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res
