# 把string分成多个片段放进list里，每个片段长度为k
# 把每两个片段中的第一个reverse，第二个不动
# 把所有片段join一下
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
		# Divide s into an array of substrings length k
        s = [s[i:i+k] for i in range(0,len(s),k)]
		# Reverse every other substring, beginning with s[0]
        for i in range(0,len(s),2):
            s[i] = s[i][::-1]
		# Join array of substrings into one string and return 
        return ''.join(s)
