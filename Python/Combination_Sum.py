class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(l, n, t, idx):
            if t == 0:
                res.append(l)
                return
            if t < 0:
                return
            for i in range(idx, len(n)):
                backtrack(l+[n[i]], n, t-n[i], i)
        backtrack([], candidates, target, 0)
        return res
