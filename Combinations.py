class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(l, n, k):
            if k == 0:
                res.append(l)
            for i in range(1,n+1):
                backtrack(l+[i], i-1, k-1)
        backtrack([], n, k)
        return res
