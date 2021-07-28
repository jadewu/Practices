# 一维dp，记录s的每个字节处，是否满足前面的string可以分成wordDict里面的词
# s[i]的dp值，就是s[i-len(w)]的dp值，和s[i-len(w)+1:i+1]是否在wordDict里，来一起判断的
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1]:
                    if dp[i-len(w)] or i-len(w)+1 == 0:
                        dp[i] = True
        return dp[len(s)-1]
