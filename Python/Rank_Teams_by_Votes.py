# 记录每个字符在所有位置出现的次数
# 因为要按出现次数从大到小排列，所以可以在记录次数的时候按-1来记
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        counter = {k:[0]*len(votes[0]) for k in votes[0]}
        for val in votes:
            for i,ch in enumerate(val):
                counter[ch][i]-=1 # - as we need to sort in reverse
        sorted_counter = sorted(counter.items(), key=lambda k:(k[1],k[0]))
        ans = ""
        for ch,_ in sorted_counter:
            ans+=ch
        return ans
