# use a list to store current longest substring
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        l = []
        for i in s:
            if i not in l:
                l.append(i)
            else:
                if len(l) > res:
                    res = len(l)
                l = l[l.index(i)+1:]
                l.append(i)
        return max(len(l),res)

# Use sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start = 0, 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            d[s[i]] = i
        return res

# Use dictionary to store current longest substring and the position of each char
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        c = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if c > res:
                    res = c
                l = len(d)
                d = {key:val for key, val in d.items() if val > d[s[i]]}
                for k, v in d.items():
                    d[k] = v - (l - len(d)) 
                c = len(d) + 1
                d[s[i]] = c 
            else:
                c += 1
                d[s[i]] = c
        #    print(d)
        return max(c,res)
