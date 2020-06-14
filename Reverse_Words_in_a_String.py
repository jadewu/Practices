class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        if not l:
            return ""
        i, j = 0, len(l)-1
        while i < j:
            l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        res = ""
        for i in range(len(l)-1):
            res += l[i] + " "
        res += l[-1]
        return res
