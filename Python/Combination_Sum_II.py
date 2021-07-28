class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(l, c, t, idx):
            if t == 0:
                res.append(l)
                return
            if t < 0:
                return
            for i in range(idx, len(c)):
                # 这一步可以去重，当除了idx以外碰到重复的数，就不再做backtrack
                if (i > idx) and (c[i] == c[i-1]):
                    continue
                backtrack(l+[c[i]], c, t-c[i], i+1)
        backtrack([], candidates, target, 0)
        return res
