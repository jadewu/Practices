class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0
        if not k:
            return 0
        i = 0
        res = 0
        l = ['a', 'e', 'i', 'o', 'u']
        for w in range(k):
            if s[w] in l:
                res += 1
        i = 1
        a = res
        while i < len(s) - k + 1:
            if s[i-1] in l:
                a -= 1
            if s[i+k-1] in l:
                a += 1                
            res = max(res, a)
            i += 1
        return res
