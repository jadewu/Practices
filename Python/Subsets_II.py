class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for num in nums:
            m = len(res)
            for i in range(m):
                res += [res[i] + [num]]
                
        ans = []
        for i in res:
            if i not in ans:
                ans.append(i)

        return ans
